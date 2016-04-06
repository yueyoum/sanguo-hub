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

class Data():
    pass

def _object_maker(s):
    with open(os.path.join(FIXTURES_PATH, s), 'r') as f:
        content = json.loads(f.read())

    res = {}
    for c in content:
        d = Data()
        d.id = c['pk']
        for k, v in c['fields'].iteritems():
            setattr(d, k, v)

        res[d.id] = d

    return res


HEROS = _make_data('heros.json')
EQUIPMENTS = _make_data('equipments.json')
GEMS = _make_data('gems.json')
STUFFS = _make_data('stuffs.json')
HORSES = _make_data('horse.json')
RESOURCE_TYPE = _make_data('resource_type.json')
PURCHASES_CHOICE = _make_data('purchase.json')

PURCHASES = _object_maker('purchase.json')

def _transform_ios_id():
    res = {}
    for k, v in PURCHASES.iteritems():
        res[v.ios_id] = v
    return res

PURCHASES_BY_IOS_ID = _transform_ios_id()
