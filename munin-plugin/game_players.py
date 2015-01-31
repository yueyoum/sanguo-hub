# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '15-1-31'

import os
import sys

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.dirname(CURRENT_PATH)

sys.path.append(PROJECT_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = 'hub.settings'


from apps.account.models import Account
from apps.character.models import Character

print "accounts.value", Account.objects.count()
print "characters.value", Character.objects.count()

