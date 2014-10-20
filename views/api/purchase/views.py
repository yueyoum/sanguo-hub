# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-6-30'

from utils.decorate import json_return
from core.purchase import purchase_ios_verify

from apps.purchase.models import Purchase91Log
from preset import errormsg


@json_return
def ios_verify(request):
    try:
        server_id = int(request.POST['server_id'])
        char_id = int(request.POST['char_id'])
        receipt = request.POST['receipt']
    except:
        return {'ret': errormsg.BAD_MESSAGE}

    return purchase_ios_verify(server_id, char_id, receipt)



@json_return
def get_purchase91_order_id(request):
    server_id = int(request.POST['server_id'])
    char_id = int(request.POST['char_id'])
    goods_id = int(request.POST['goods_id'])

    order_id = Purchase91Log.make_order_id(server_id, char_id, goods_id)
    # if not order_id:
    #     return {'ret': errormsg.PURCHASE_91_NOT_CONFIRM}

    return {
        'ret': 0,
        'data': {
            'order_id': order_id
        }
    }



@json_return
def purchase91_confirm(request):
    char_id = int(request.POST['char_id'])

    data = {
        'ret': 0,
        'data': {
            'status': 0,
            'goods_id': 0,
        }
    }

    # 这里只取最后一个订单
    p = Purchase91Log.objects.filter(char_id=char_id).order_by('-order_time')[0:1]
    if p.count() == 0:
        return data

    p = p[0]

    data['data']['goods_id'] = p.goods_id
    if p.pay_status == 1:
        # success
        return data

    # error code
    data['ret'] = errormsg.PURCHASE_91_FAILURE
    if p.pay_status == -1:
        # WAITING
        data['data']['status'] = 1
    elif p.pay_status == 0:
        # FAILURE
        data['data']['status'] = 2

    return data
