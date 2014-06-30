# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/21/14'

import json
from base64 import b64encode

import requests

from apps.character.models import Character
from apps.purchase.models import Products, PurchaseSuccessLog, PurchaseFailureLog

from preset import errormsg


VERITY_URL = 'https://buy.itunes.apple.com/verifyReceipt'
VERITY_URL_TEST = 'https://sandbox.itunes.apple.com/verifyReceipt'


def get_product_list():
    products = {}
    for p in Products.objects.all():
        products[p.id] = {
            'name': p.name,
            'des': p.des,
            'sycee': p.sycee,
            'actual_sycee': p.actual_sycee,
        }
    return products



class RequestsNotOK(Exception):
    pass


def _do_verify(receipt):
    """

    :param receipt:
    :return: (return_code, apple_response)
    :rtype : (int, dict)
    """
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
    except:
        return (errormsg.PURCHASE_APPLE_ERROR, "")

    if res['status'] == 21007:
        # 测试的交易凭证，却发到了正式服务器去验证
        try:
            res = _do(VERITY_URL_TEST)
        except:
            return (errormsg.PURCHASE_APPLE_ERROR, "")

    if res['status'] != 0:
        print "Verify Failure. {0}".format(res)
        return (errormsg.PURCHASE_VERIFY_ERROR, "")

    return (0, res)


class Purchase(object):
    def __init__(self, char_id):
        self.char_id = char_id


    def verify(self, receipt):
        try:
            c = Character.objects.get(id=self.char_id)
        except Character.DoesNotExist:
            return {'ret': errormsg.CHARACTER_NOT_FOUND}

        data = {
            'char_id': self.char_id,
            'receipt': receipt,
        }

        err_code, res = _do_verify(receipt)
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
            self.save_purchase_failure_log(data)

            return {'ret': err_code}

        product_id = res['receipt']['product_id']
        quantity = int(res['receipt']['quantity'])

        products = get_product_list()

        data['product_id'] = product_id
        data['actual_sycee'] = products[product_id]['actual_sycee']
        data['quantity'] = quantity
        data['bvrs'] = res['receipt']['bvrs']

        log_id = self.save_purchase_success_log(data)

        add_sycee = products[product_id]['actual_sycee'] * quantity

        return {
            'ret': 0,
            'data': {
                'log_id': log_id,
                'char_id': self.char_id,
                'product_id': product_id,
                'name': products[product_id]['name'],
                'sycee': add_sycee,
                'actual_sycee': add_sycee
            }
        }


    def save_purchase_failure_log(self, data):
        PurchaseFailureLog.objects.create(
            char_id=data['char_id'],
            receipt=data['receipt'],
            inner_error=data['inner_error'],
            apple_error=data['apple_error'],
        )

    def save_purchase_success_log(self, data):
        p = PurchaseSuccessLog.objects.create(
            char_id=data['char_id'],
            receipt=data['receipt'],
            product_id=data['product_id'],
            actual_sycee=data['actual_sycee'],
            quantity=data['quantity'],
            bvrs=data['bvrs'],
        )
        return p.id


def set_done(log_id):
    PurchaseSuccessLog.objects.filter(id=log_id).update(send_done=True)
