# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/21/14'

import json
from base64 import b64encode

import requests

from apps.character.models import Character
from apps.purchase.models import Products, PurchaseSuccessLog, PurchaseFailureLog

from core.server import SERVERS


VERITY_URL = 'https://buy.itunes.apple.com/verifyReceipt'
VERITY_URL_TEST = 'https://sandbox.itunes.apple.com/verifyReceipt'


def _products():
    ps = {}
    for p in Products.objects.all():
        ps[p.id] = {
            'name': p.name,
            'des': p.des,
            'sycee': p.sycee,
            'actual_sycee': p.actual_sycee,
        }
    return ps

PRODUCTS = _products()




class RequestsNotOK(Exception):
    pass


class Purchase(object):
    def __init__(self, char_id):
        self.char_id = char_id


    def _do_verify(self, receipt):
        data = json.dumps({
            'receipt-data': b64encode(receipt)
        })

        def _do(url):
            req = requests.post(url, data=data, timeout=5)
            if not req.ok:
                raise RequestsNotOK("requests not ok")
            return req.json()


        try:
            res = _do(VERITY_URL)
        except Exception as e:
            print e
            return (1, "")

        print res
        if res['status'] == 21007:
            # 测试的交易凭证，却发到了正式服务器去验证

            try:
                res = _do(VERITY_URL_TEST)
            except Exception as e:
                print e
                return (1, "")

            print res
            if res['status'] != 0:
                return (res['status'], "")

        return (0, res)


    def verify(self, receipt):
        print receipt

        try:
            c = Character.objects.get(id=self.char_id)
        except Character.DoesNotExist:
            return (2, "")

        data = {
            'product_id': 'xxx',
            'char_id': self.char_id,
            'receipt': receipt,
        }

        err_code, res = self._do_verify(receipt)
        if err_code:
            # FIXME error return
            if err_code > 20000:
                inner_error = 0
                apple_error = err_code
            else:
                inner_error = err_code
                apple_error = 0

            data['inner_error'] = inner_error
            data['apple_error'] = apple_error
            self.save_purchase_log(data)

            # FIXME error code
            print "verify error"
            return (2, "")


        product_id = res['receipt']['product_id']
        quantity = res['receipt']['quantity']

        data['quantity'] = quantity
        data['bvrs'] = res['receipt']['bvrs']

        log_id = self.save_purchase_log(data)


        # cal server api to send sycee
        s = SERVERS[c.server_id]
        data = {
            'char_id': self.char_id,
            'sycee': PRODUCTS[product_id]['actual_sycee'] * quantity
        }
        req = requests.post('{0}:{1}/api/purchase/done/'.format(s['url'], s['port']), data=data)
        if not req.ok:
            return (2, "")

        res = req.json()
        if res['ret'] != 0:
            return (2, "")

        self.set_send_done(log_id)

        return (0, product_id)


    def save_purchase_log(self, data):
        # data like this:
        # {
        #     'product_id': '',
        #     'char_id': 0,
        #     'receipt': '',
        #
        #     'inner_error': *,
        #     'apple_error': *,
        #
        #     'quantity': *,
        #     'bvrs': *,
        # }
        #

        # 打 * 号的意思是不一定有

        if 'inner_error' in data or 'apple_error' in data:
            # failure
            p = PurchaseFailureLog.objects.create(
                product_id=data['product_id'],
                actual_sycee=data['actual_sycee'],
                char_id=data['char_id'],
                receipt=data['receipt'],

                inner_error=data['inner_error'],
                apple_error=data['apple_error'],
            )

            log_id = p.id
        else:
            # success
            p = PurchaseSuccessLog.objects.create(
                product_id=data['product_id'],
                actual_sycee=data['actual_sycee'],
                char_id=data['char_id'],
                receipt=data['receipt'],

                quantity=data['quantity'],
                bvrs=data['bvrs'],
            )

            log_id = p.id

        return log_id


    def set_send_done(self, log_id):
        PurchaseSuccessLog.objects.filter(id=log_id).update(send_done=True)

