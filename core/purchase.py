# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/21/14'

from apps.purchase.models import Products, PurchaseSuccessLog, PurchaseFailureLog
from core.exception import APIDataError

def _products():
    ps = {}
    for p in Products.objects.all():
        ps[p.id] = {
            'name': p.name,
            'des': p.des,
            'gold': p.gold,
            'actual_sycee': p.actual_sycee,
        }
    return ps

PRODUCTS = _products()



def _parse_post_log_data(data):
    x = {}
    product_id = data['product_id']
    if product_id not in PRODUCTS:
        raise APIDataError()

    x['product_id'] = product_id
    x['actual_sycee'] = PRODUCTS['product_id']['actual_sycee']
    x['char_id'] = data['char_id']
    x['receipt'] = data['receipt']

    if 'inner_error' in data or 'apple_error' in data:
        x['inner_error'] = data.get('inner_error', 0)
        x['apple_error'] = data.get('apple_error', 0)
    else:
        x['quantity'] = data['quantity']
        x['bvrs'] = data['bvrs']

    return x



def save_purchase_log(data):
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

    try:
        data = _parse_post_log_data(data)
    except (KeyError, APIDataError):
        return {'ret': 1}

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

    return {
        'ret': 0,
        'data': {
            'log_id': log_id
        }
    }


def set_send_done(data):
    log_id=int(data['log_id'])
    PurchaseSuccessLog.objects.filter(id=log_id).update(send_done=True)

