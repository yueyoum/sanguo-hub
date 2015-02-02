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
from apps.server.models import Server
from apps.purchase.models import PurchaseAiyingyongLog

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
    print "graph_order sum",

    servers = Server.objects.filter(is_test=False).all()

    for s in servers:
        print "server{0}".format(s.id),
    print

    print "sum.label sum"
    print "sum.draw LINE0"
    print "sum.info total purchase money"

    for s in servers:
        print "server{0}.label server{0}".format(s.id)
        print "server{0}.draw AREASTACK".format(s.id)
        print "server{0}.info purchase money of server {0}".format(s.id)

    sys.exit(0)

# value
print "sum.value", PurchaseAiyingyongLog.objects.aggregate(Sum('order_money'))['order_money__sum']
for s in Server.objects.filter(is_test=False).all():
    print "server{0}.value".format(s.id), PurchaseAiyingyongLog.objects.filter(server_id=s.id).aggregate(Sum('order_money'))['order_money__sum']

