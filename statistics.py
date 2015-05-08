# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       statistics
Date Created:   2015-05-08 15:59
Description:

"""

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'hub.settings'

import arrow
from django.db.models import Q, Sum
from apps.account.models import Account
from apps.purchase.models import (
    PurchaseJodoPlayLog,
    PurchaseAiyingyongLog,
)

FORMAT = "YYYY-MM-DD HH:mm:ssZ"

def day_new_account(start, days):
    print "日新增用户"
    for i in range(days):
        day = arrow.get(start).replace(days=i)
        next_day = day.replace(days=1)

        condition = Q(register_at__gte=day.format(FORMAT)) & Q(register_at__lte=next_day.format(FORMAT))

        print day.format("YYYY-MM-DD"),
        print Account.objects.filter(condition).count()

def day_purchase_account_jodo(start, days):
    print "日充值用户"
    for i in range(days):
        day = arrow.get(start).replace(days=i)
        next_day = day.replace(days=1)

        condition = Q(order_time__gte=day.format(FORMAT)) & Q(order_time__lte=next_day.format(FORMAT))

        print day.format("YYYY-MM-DD"),
        print PurchaseJodoPlayLog.objects.filter(condition).count()

def day_purchase_money_jodo(start, days):
    print "日充值金额"
    for i in range(days):
        day = arrow.get(start).replace(days=i)
        next_day = day.replace(days=1)

        condition = Q(order_time__gte=day.format(FORMAT)) & Q(order_time__lte=next_day.format(FORMAT))

        print day.format("YYYY-MM-DD"),
        money = PurchaseJodoPlayLog.objects.filter(condition).aggregate(Sum('jodo_price'))['jodo_price__sum']
        print money / 5 if money else 0

def day_purchase_account_aiyingyong(start, days):
    print "日充值用户"
    for i in range(days):
        day = arrow.get(start).replace(days=i)
        next_day = day.replace(days=1)

        condition = Q(order_time__gte=day.format(FORMAT)) & Q(order_time__lte=next_day.format(FORMAT))

        print day.format("YYYY-MM-DD"),
        print PurchaseAiyingyongLog.objects.filter(condition).count()


def day_purchase_money_aiyingyong(start, days):
    print "日充值金额"
    for i in range(days):
        day = arrow.get(start).replace(days=i)
        next_day = day.replace(days=1)

        condition = Q(order_time__gte=day.format(FORMAT)) & Q(order_time__lte=next_day.format(FORMAT))

        print day.format("YYYY-MM-DD"),
        money = PurchaseAiyingyongLog.objects.filter(condition).aggregate(Sum('order_money'))['order_money__sum']
        print money if money else 0


if __name__ == '__main__':
    platform = os.getenv("PLATFORM")
    start = "2015-04-01 00:00:00+0800"
    days = 30

    day_new_account(start, days)
    if platform == 'jodo':
        day_purchase_account_jodo(start, days)
        day_purchase_money_jodo(start, days)
    elif platform == 'aiyingyong':
        day_purchase_account_aiyingyong(start, days)
        day_purchase_money_aiyingyong(start, days)

