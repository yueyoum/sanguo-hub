# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/21/14'

from core.purchase import PRODUCTS, save_purchase_log, set_send_done
from utils.decorate import json_return

@json_return
def get_products(request):
    return {
        'ret': 0,
        'data': {
            'products': PRODUCTS
        }
    }


@json_return
def save_log(request):
    return save_purchase_log(request.POST)

@json_return
def send_done(request):
    set_send_done(request.POST)
    return {'ret': 0}
