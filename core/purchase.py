# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/21/14'

import json
from base64 import b64encode

import requests
from core.fixtures import PURCHASES_BY_IOS_ID
from apps.purchase.models import PurchaseIOSErrorLog, PurchaseIOSSuccessLog
from preset import errormsg


VERITY_URL = 'https://buy.itunes.apple.com/verifyReceipt'
VERITY_URL_TEST = 'https://sandbox.itunes.apple.com/verifyReceipt'



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
        req = requests.post(url, data=data, timeout=8)
        if not req.ok:
            raise RequestsNotOK("requests not ok")
        return req.json()

    try:
        res = _do(VERITY_URL)
    except:
        return (errormsg.PURCHASE_VERIFY_ERROR, "")

    if res['status'] == 21007:
        # 测试的交易凭证，却发到了正式服务器去验证
        try:
            res = _do(VERITY_URL_TEST)
        except:
            return (errormsg.PURCHASE_VERIFY_ERROR, "")

    if res['status'] != 0:
        print "==== VERIFY ERROR ===="
        print res
        return (errormsg.PURCHASE_VERIFY_ERROR, "")

    return (0, res)



def purchase_ios_verify(server_id, char_id, receipt):
    err_code, res = _do_verify(receipt)
    if err_code:
        PurchaseIOSErrorLog.objects.create(
            server_id=server_id,
            char_id=char_id,
            error_code=err_code,
            receipt=receipt
        )
        return {'ret': err_code}

    product_id = res['receipt']['product_id']
    quantity = int(res['receipt']['quantity'])
    bvrs = res['receipt']['bvrs']
    unique_identifier = res['receipt']['unique_identifier']

    if PurchaseIOSSuccessLog.objects.filter(unique_identifier=unique_identifier).exists():
        return {'ret', errormsg.PURCHASE_ALREADY_VERIFIED}

    order_money = PURCHASES_BY_IOS_ID[product_id].rmb
    # ALL OK
    PurchaseIOSSuccessLog.objects.create(
        unique_identifier=unique_identifier,
        server_id=server_id,
        char_id=char_id,
        product_id=product_id,
        quantity=quantity,
        bvrs=bvrs,
        receipt=receipt,
        order_money=order_money
    )

    return {
        'ret': 0,
        'data': {
            'goods_id': PURCHASES_BY_IOS_ID[product_id].id
        }
    }
