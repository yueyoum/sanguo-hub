# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-6-30'

from utils.decorate import json_return
from core.purchase import purchase_ios_verify, purchase_allsdk_verify

from apps.purchase.models import Purchase91Log, PurchaseAiyingyongLog, PurchaseJodoPlayLog
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
def allsdk_verify(request):
    try:
        server_id = int(request.POST['server_id'])
        char_id = int(request.POST['char_id'])
        sn = request.POST['sn']
        goods_id = int(request.POST['goods_id'])
        platform = request.POST['platform']
    except:
        return {'ret': errormsg.BAD_MESSAGE}

    return purchase_allsdk_verify(server_id, char_id, sn, goods_id, platform)


@json_return
def get_purchase_order_id(request):
    server_id = int(request.POST['server_id'])
    char_id = int(request.POST['char_id'])
    goods_id = int(request.POST['goods_id'])
    platform = request.POST['platform']

    if platform == '91':
        order_id = Purchase91Log.make_order_id(server_id, char_id, goods_id)
    elif platform == 'jodoplay':
        order_id = PurchaseJodoPlayLog.make_order_id(server_id, char_id, goods_id)
    else:
        return {'ret': errormsg.BAD_MESSAGE}

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


@json_return
def purchase_aiyingyong_confirm(request):
    char_id = int(request.POST['char_id'])

    data = {
        'ret': 0,
        'data': {
            'status': 0,
            'goods_id': 0,
        }
    }

    p = PurchaseAiyingyongLog.objects.filter(char_id=char_id).filter(confirmed=False).order_by('-order_time')[0:1]
    if p.count() == 0:
        # WAITING
        data['ret'] = errormsg.PURCHASE_91_FAILURE
        data['data']['status'] = 1
        return data

    p = p[0]
    data['data']['goods_id'] = p.goods_id

    if p.pay_status == 1:
        # SUCCESS
        pass
    else:
        # FAILURE
        data['ret'] = errormsg.PURCHASE_91_FAILURE
        data['data']['status'] = 2

    p.confirmed = True
    p.save()
    return data

@json_return
def purchase_jodoplay_confirm(request):
    char_id = int(request.POST['char_id'])

    data = {
        'ret': 0,
        'data': {
            'status': 0,
            'goods_id': 0,
        }
    }

    p = PurchaseJodoPlayLog.objects.filter(char_id=char_id).order_by('-order_time')[0:1]
    if p.count() == 0:
        # WAITING
        data['ret'] = errormsg.PURCHASE_91_FAILURE
        data['data']['status'] = 1
        return data

    p = p[0]
    data['data']['goods_id'] = p.goods_id

    p.confirmed = True
    p.save()
    return data

