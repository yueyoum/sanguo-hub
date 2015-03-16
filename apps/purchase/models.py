# -*- coding: utf-8 -*-

import uuid
from django.db import models


# IOS平台
class PurchaseIOSErrorLog(models.Model):
    server_id = models.IntegerField("服务器ID")
    char_id = models.IntegerField("角色ID")
    error_code = models.IntegerField("错误码")

    receipt = models.TextField()
    buy_time = models.DateTimeField("购买时间", auto_now_add=True)

    class Meta:
        db_table = 'purchase_ios_error_log'
        verbose_name = "IOS充值失败记录"
        verbose_name_plural = "IOS充值失败记录"


class PurchaseIOSSuccessLog(models.Model):
    transaction_id = models.CharField(max_length=255, unique=True)

    server_id = models.IntegerField("服务器ID", db_index=True)
    char_id = models.IntegerField("角色ID", db_index=True)

    product_id = models.CharField("商品ID", max_length=255)
    quantity = models.IntegerField("数量")

    receipt = models.TextField()

    order_money = models.FloatField("支付价格")
    buy_time = models.DateTimeField("购买时间", auto_now_add=True)

    class Meta:
        db_table = 'purchase_ios_success_log'
        verbose_name = "IOS充值成功记录"
        verbose_name_plural = "IOS充值成功记录"



# 91平台
class Purchase91Log(models.Model):
    PAY_STATUS = (
        (-1, '创建订单'),
        (0, '确认失败'),
        (1, '确认成功'),
    )

    order_id = models.CharField("订单号", max_length=255)
    order_time = models.DateTimeField("订单创建时间", auto_now_add=True, db_index=True)
    server_id = models.IntegerField("服务器ID", db_index=True)
    char_id = models.IntegerField("角色ID", db_index=True)
    goods_id = models.IntegerField("商品ID")
    # 这里server_id 和 char_id 其实是一一对应的，都记录仅仅是为了统计需要
    is_test_mode = models.BooleanField("测试模式", db_index=True)

    consume_stream_id = models.CharField("消费流水号", max_length=255)
    uid = models.CharField("91帐号ID", max_length=255)
    original_money = models.FloatField("原始总价")
    order_money = models.FloatField("实际总价")
    note = models.CharField("支付描述", max_length=255)
    pay_status = models.IntegerField("支付状态", choices=PAY_STATUS)
    create_time = models.CharField("支付时间", max_length=255)

    class Meta:
        db_table = 'purchase91_log'
        verbose_name = '91充值记录'
        verbose_name_plural = '91充值记录'

    @classmethod
    def make_order_id(cls, server_id, char_id, goods_id):
        order_id = str(uuid.uuid4())
        cls.objects.create(
            order_id=order_id,
            server_id=server_id,
            char_id=char_id,
            goods_id=goods_id,
            is_test_mode=False,

            consume_stream_id='',
            uid='',
            original_money=0,
            order_money=0,
            note='',
            pay_status=-1,
            create_time='',
        )

        return order_id


# aiyingyong
class PurchaseAiyingyongLog(models.Model):
    PAY_STATUS = (
        (1, '成功'),
        (2, '失败')
    )

    order_id = models.CharField("订单ID", max_length=255, db_index=True)
    order_time = models.DateTimeField("支付时间", auto_now_add=True)
    server_id = models.IntegerField("服务器ID", db_index=True)
    char_id = models.IntegerField("角色ID", db_index=True)
    goods_id = models.IntegerField("商品ID")

    order_money = models.FloatField("支付价格")
    pay_status = models.IntegerField("状态", choices=PAY_STATUS)
    confirmed = models.BooleanField("确认", default=False)

    class Meta:
        db_table = 'purchase_aiyingyong'
        verbose_name = '爱应用充值记录'
        verbose_name_plural = '爱应用充值记录'


# allsdk
class PurchaseAllSdkLog(models.Model):
    sn = models.CharField("交易序号", max_length=255, db_index=True)
    return_code = models.CharField("交易结果")

    order_time = models.DateTimeField("支付时间", auto_now_add=True)
    server_id = models.IntegerField("服务器ID", db_index=True)
    char_id = models.IntegerField("角色ID", db_index=True)
    goods_id = models.IntegerField("商品ID")

    order_money = models.FloatField("支付价格")

    verify_ok = models.BooleanField(default=False)

    class Meta:
        db_table = 'purchase_allsdk'
        verbose_name = "AllSDK充值记录"
        verbose_name_plural = "AllSDK充值记录"
