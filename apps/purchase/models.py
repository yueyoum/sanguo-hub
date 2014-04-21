# -*- coding: utf-8 -*-

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
    product_id = models.CharField(max_length=255)
    actual_sycee = models.IntegerField("实际元宝")
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
    quantity = models.IntegerField("数量")
    bvrs = models.CharField("版本号", max_length=255)
    send_done = models.BooleanField("成功给出物品", default=False)

    class Meta:
        db_table = 'purchase_log_success'
        verbose_name = '交易成功记录'
        verbose_name_plural = '交易成功记录'

