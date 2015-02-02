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
from apps.character.models import Character


try:
    arg = sys.argv[1]
except IndexError:
    arg = ""

if arg == 'autoconf':
    print "yes"
    sys.exit(0)

if arg == 'config':
    print "graph_title Game Servers Chars Amount"
    print "graph_args --base 1000 -l 0"
    print "graph_scale yes"
    print "graph_vlabel Chars Amount"
    print "graph_category game"
    print "graph_info This graph shows the Servers Chars Amount"
    print "graph_order",

    servers = Server.objects.filter(is_test=False).all()

    for s in servers:
        print "server{0}".format(s.id),

    print

    for s in servers:
        print "server{0}.label server{0}".format(s.id)
        print "server{0}.draw LINE1".format(s.id)
        print "server{0}.info All Characters amount of server{0}".format(s.id)

    sys.exit(0)


# value
for s in Server.objects.filter(is_test=False).all():
    print "server{0}.value".format(s.id), Character.objects.filter(server_id=s.id).count()

