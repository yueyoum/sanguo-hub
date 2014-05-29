# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'

from django.db import transaction, IntegrityError

from apps.character.models import Character
from core.exception import GateException
from core.server import SERVERS
from utils.decorate import json_return
from preset import errormsg

from utils.api import apicall
from libs.apiclient import APIFailure

@json_return
def create(request):
    try:
        account_id = int(request.POST['account_id'])
        server_id = int(request.POST['server_id'])
        name = request.POST['name']
    except (KeyError, ValueError):
        return {'ret': errormsg.BAD_MESSAGE}

    if len(name) > 7:
        return {'ret': errormsg.CHAR_NAME_TOO_LONG}

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

            s = SERVERS[server_id]
            try:
                res = apicall(data=data, cmd='{0}:{1}/api/character/initialize/'.format(s['url'], s['port']))
            except APIFailure:
                raise GateException("Char Initialize Failure in Server: {0}".format(server_id))

            if res['ret'] != 0:
                raise GateException("Char Initialize Failure in Server: {0}. ret is {1}".format(server_id, res['ret']))

    except IntegrityError as e:
        if 'account_id' in e.args[1]:
            return {'ret': errormsg.CHAR_ALREADY_EXIST}
        return {'ret': errormsg.CHAR_NAME_HAS_BEEN_TAKEN}
    except GateException as e:
        return {'ret': errormsg.CHAR_CREATE_FAUILER}

    return {
        'ret': 0,
        'data': {
            'char_id': char.id
        }
    }
