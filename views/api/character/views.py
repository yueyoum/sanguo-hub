# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'

import requests
from django.db import transaction, IntegrityError

from apps.character.models import Character
from apps.server.models import Server
from core.exception import GateException
from utils.decorate import json_return

@json_return
def create(request):
    try:
        account_id = int(request.POST['account_id'])
        server_id = int(request.POST['server_id'])
        name = request.POST['name']
    except (KeyError, ValueError):
        return {'ret': 1}

    if len(name) > 7:
        return {'ret': 30}

    try:
        with transaction.atomic():
            char = Character.objects.create(
                account_id=account_id,
                server_id=server_id,
                name=name,
            )

            # FIXME
            data = {
                'account_id': account_id,
                'server_id': server_id,
                'char_id': char.id,
                'name': name
            }
            this_server = Server.objects.select_related('node').get(id=server_id)

            x = requests.post('{0}:{1}/api/character/initialize/'.format(this_server.node.url, this_server.node.port), data=data)
            res = x.json()
            if res['ret'] != 0:
                raise GateException("char initialize failure")

            # XXX
            guide_server = Server.objects.select_related('node').get(id=0)
            x = requests.post('{0}:{1}/api/character/initialize/'.format(guide_server.node.url, guide_server.node.port), data=data)
            res = x.json()
            if res['ret'] != 0:
                raise GateException("char initialize failure")

    except IntegrityError as e:
        if 'account_id' in e.args[1]:
            return {'ret': 31}
        return {'ret': 32}
    except GateException:
        return {'ret': 33}

    return {
        'ret': 0,
        'data': {
            'char_id': char.id
        }
    }

