# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-7-24'

import json
import hashlib
import traceback

from django.conf import settings
from django.http import HttpResponse

from apps.purchase.models import Purchase91Log

from utils.api import api_purchase91_done

def purchase_91_notify(request):
    try:
        appid = request.GET['AppId']
        act = request.GET['Act']
        product_name = request.GET['ProductName']
        consume_stream_id = request.GET['ConsumeStreamId']
        order_id = request.GET['CooOrderSerial']
        uid = request.GET['Uin']
        goods_id = request.GET['GoodsId']
        goods_info = request.GET['GoodsInfo']
        goods_count = request.GET['GoodsCount']
        original_money = request.GET['OriginalMoney']
        order_money = request.GET['OrderMoney']
        note = request.GET['Note']
        pay_status = request.GET['PayStatus']
        create_time = request.GET['CreateTime']
        sign = request.GET['Sign']
    except:
        print "----Error----"
        print request.GET
        traceback.print_exc()

        data = {
            'ErrorCode': 4,
            'ErrorDesc': "参数无效"
        }
        return HttpResponse(json.dumps(data), content_type='application/json')

    if act != '1':
        data = {
            'ErrorCode': 3,
            'ErrorDesc': "Act无效"
        }
        return HttpResponse(json.dumps(data), content_type='application/json')


    settings91 = settings.THIRD_PLATFORM['91']

    settings_appid = settings91['appid']
    settings_appkey = settings91['appkey']

    if settings_appid != appid:
        data = {
            'ErrorCode': 2,
            'ErrorDesc': "AppId无效",
        }
        return HttpResponse(json.dumps(data), content_type='application/json')


    my_sign_text = u'{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}{13}{14}'.format(
        appid,
        act,
        product_name,
        consume_stream_id,
        order_id,
        uid,
        goods_id,
        goods_info,
        goods_count,
        original_money,
        order_money,
        note,
        pay_status,
        create_time,
        settings_appkey
    )

    my_sign = hashlib.md5(my_sign_text.encode('utf-8')).hexdigest()

    if my_sign != sign:
        data = {
            'ErrorCode': 5,
            'ErrorDesc': "Sign无效",
        }
        return HttpResponse(json.dumps(data), content_type='application/json')

    try:
        p = Purchase91Log.objects.get(order_id=order_id)
    except Purchase91Log.DoesNotExist:
        print "----Warning----"
        print "Order id {0} Does Not Exist. Ignore".format(order_id)
        data = {
            'ErrorCode': 1,
            'ErrorDesc': "接收成功",
        }

        return HttpResponse(json.dumps(data), content_type='application/json')

    p.is_test_mode = request.path == '/callback/test91/'
    p.consume_stream_id = consume_stream_id
    p.uid = uid
    p.original_money = float(original_money)
    p.order_money = float(order_money)
    p.note = note
    p.pay_status = int(pay_status)
    p.create_time = create_time
    p.save()

    api_purchase91_done(p.server_id, p.char_id, p.goods_id)

    data = {
        'ErrorCode': 1,
        'ErrorDesc': "接收成功",
    }

    return HttpResponse(json.dumps(data), content_type='application/json')
