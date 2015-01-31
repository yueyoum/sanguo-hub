# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '15-1-31'

import os
import sys

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.dirname(CURRENT_PATH)

sys.path.append(PROJECT_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = 'hub.settings'


from django.db.models import Sum
from apps.purchase.models import PurchaseAiyingyongLog

print "order_amount.value", PurchaseAiyingyongLog.objects.count()
print "char_amount.value", PurchaseAiyingyongLog.objects.values_list('char_id', flat=True).distinct().count()
print "sum.value", PurchaseAiyingyongLog.objects.aggregate(Sum('order_money'))['order_money__sum']


