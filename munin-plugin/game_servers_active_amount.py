# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '15-1-31'

import os
import sys

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.dirname(CURRENT_PATH)

sys.path.append(PROJECT_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = 'hub.settings'

from apps.server.models import Server


try:
    arg = sys.argv[1]
except IndexError:
    arg = ""

if arg == 'autoconf':
    print "yes"
    sys.exit(0)

if arg == 'config':
    print "graph_title Game Servers Active Amount"
    print "graph_args --base 1000 -l 0"
    print "graph_scale yes"
    print "graph_vlabel Active amount"
    print "graph_category game"
    print "graph_info This graph shows the Servers Active Amount"
    print "graph_order",

    for s in Server.objects.filter(is_test=False).all():
        print "server{0}".format(s.id),

    print


    for s in Server.objects.filter(is_test=False).all():
        print "server{0}.label server{0}".format(s.id)
        print "server{0}.draw AREASTACK".format(s.id)
        print "server{0}.info Active amount of server{0}".format(s.id)

    sys.exit(0)


# value
for s in Server.objects.filter(is_test=False).all():
    print "server{0}.value".format(s.id), s.active_players

