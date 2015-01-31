# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '15-1-31'

import os
import sys

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.dirname(CURRENT_PATH)

sys.path.append(PROJECT_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = 'hub.settings'


def execute():
    from apps.account.models import Account
    from apps.character.models import Character

    print "accounts.value", Account.objects.count()
    print "characters.value", Character.objects.count()


try:
    arg = sys.argv[1]
except IndexError:
    arg = ""


if arg == "":
    execute()
    sys.exit(0)

if arg == 'autoconf':
    print "yes"
    sys.exit(0)

if arg == 'config':
    print "graph_title Players Amount of Game"
    print "graph_args --base 1000 -l 0"
    print "graph_scale yes"
    print "graph_vlabel Players amount"
    print "graph_category game"
    print "graph_info This graph shows the number of Accounts/Characters"
    print "graph_order accounts characters"

    print "accounts.label players"
    print "accounts.draw AREA"
    print "accounts.info Amount of Accounts"
    print "characters.label characters"
    print "characters.draw STACK"
    print "characters.info Amount of Characters"

    exit(0)


