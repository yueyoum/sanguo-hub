# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-6-30'

from utils.decorate import json_return
from core.purchase import Purchase, get_product_list, set_done


@json_return
def products(request):
    data = get_product_list()
    return {
        'ret': 0,
        'data': {
            'products': data
        }
    }

@json_return
def verify(request):
    try:
        char_id = int(request.POST['char_id'])
        receipt = request.POST['receipt']
    except:
        return {'ret': 1}

    p = Purchase(char_id)
    return p.verify(receipt)


@json_return
def done(request):
    try:
        log_id = request.POST['log_id']
    except:
        return {'ret': 1}

    set_done(log_id)
    return {'ret': 0}
