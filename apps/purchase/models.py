# -*- coding: utf-8 -*-

import uuid
from django.db import models


class Products(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=32)
    des = models.CharField(max_length=255)

    sycee = models.IntegerField("元宝")
    actual_sycee = models.IntegerField("实际元宝")

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = 'products'
        verbose_name = '商品'
        verbose_name_plural = '商品'


class PurchaseLog(models.Model):
    char_id = models.IntegerField("购买者ID")
    buy_date = models.DateTimeField("购买时间", auto_now_add=True)

    receipt = models.TextField()

    class Meta:
        abstract = True


class PurchaseFailureLog(PurchaseLog):
    inner_error = models.IntegerField("内部错误代码", default=0)
    apple_error = models.IntegerField("苹果错误代码", default=0)

    class Meta:
        db_table = 'purchase_log_failure'
        verbose_name = '交易失败记录'
        verbose_name_plural = '交易失败记录'


class PurchaseSuccessLog(PurchaseLog):
    product_id = models.CharField(max_length=255)
    actual_sycee = models.IntegerField("实际元宝")
    quantity = models.IntegerField("数量")
    bvrs = models.CharField("版本号", max_length=255)
    send_done = models.BooleanField("成功给出物品", default=False)

    class Meta:
        db_table = 'purchase_log_success'
        verbose_name = '交易成功记录'
        verbose_name_plural = '交易成功记录'


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
