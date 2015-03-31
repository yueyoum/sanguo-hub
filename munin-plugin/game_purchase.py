# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '15-1-31'

import os
import sys

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.dirname(CURRENT_PATH)

sys.path.append(PROJECT_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = 'hub.settings'

PLATFORM = os.environ.get('PLATFORM', None)

from django.db.models import Sum
from apps.server.models import Server

try:
    arg = sys.argv[1]
except IndexError:
    arg = ""

if arg == 'autoconf':
    print "yes"
    sys.exit(0)

if arg == 'config':
    print "graph_title Purchase status of Game"
    print "graph_args --base 1000 -l 0"
    print "graph_scale yes"
    print "graph_vlabel Purchase"
    print "graph_category game"
    print "graph_info This graph shows the Purchase status of game"
    print "graph_order",

    servers = Server.objects.filter(is_test=False).all()

    for s in servers:
        print "server{0}".format(s.id),
    print "sum"


    for s in servers:
        print "server{0}.label server{0}".format(s.id)
        print "server{0}.draw AREASTACK".format(s.id)
        print "server{0}.info purchase money of server {0}".format(s.id)

    print "sum.label sum"
    print "sum.draw LINE0"
    print "sum.info total purchase money"

    sys.exit(0)


# value
if PLATFORM == 'aiyingyong':
    from apps.purchase.models import PurchaseAiyingyongLog

    values = 0
    for s in Server.objects.filter(is_test=False).all():
        this_value = PurchaseAiyingyongLog.objects.filter(server_id=s.id).aggregate(Sum('order_money'))['order_money__sum']
        if this_value is None:
            this_value = 0
        values += this_value
        print "server{0}.value".format(s.id), this_value

    print "sum.value", values

    sys.exit(0)

if PLATFORM == 'allsdk':
    from apps.purchase.models import PurchaseAllSdkLog

    values = 0
    for s in Server.objects.filter(is_test=False).all():
        this_value = PurchaseAllSdkLog.objects.filter(server_id=s.id).aggregate(Sum('order_money'))['order_money__sum']
        if this_value is None:
            this_value = 0
        values += this_value
        print "server{0}.value".format(s.id), this_value

    print "sum.value", values

    sys.exit(0)

if PLATFORM == 'jodo' or PLATFORM == 'jodopaly':
    from apps.purchase.models import PurchaseJodoPlayLog

    values = 0
    for s in Server.objects.filter(is_test=False).all():
        this_value = PurchaseJodoPlayLog.objects.filter(server_id=s.id).aggregate(Sum('jodo_price'))['jodo_price__sum']
        if this_value is None:
            this_value = 0
        values += this_value
        print "server{0}.value".format(s.id), this_value

    print "sum.value", values

    sys.exit(0)
