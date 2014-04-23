# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/22/14'

from core.store import newest_store_goods, Store

from libs.decorate import json_return

@json_return
def get(request):
    return {
        'ret': 0,
        'data': {
            'store': newest_store_goods()
        }
    }


@json_return
def buy(request):
    s = Store()
    return s.buy(request.POST)

