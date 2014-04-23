# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/22/14'

import os
import json

from django.conf import settings

FIXTURES_PATH = settings.FIXTURES_PATH

def _make_data(s):
    with open(os.path.join(FIXTURES_PATH, s), 'r') as f:
        data = f.read()

    data = json.loads(data)
    choose = []
    for d in data:
        choose.append((d['pk'], d['fields']['name']))
    choose.sort(key=lambda item: item[0])
    return choose

HEROS = _make_data('heros.json')
EQUIPMENTS = _make_data('equipments.json')
GEMS = _make_data('gems.json')
STUFFS = _make_data('stuffs.json')
