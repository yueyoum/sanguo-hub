# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'

from django.http import HttpResponse
from django.db import IntegrityError

from apps.character.models import Character

from utils.decorate import json_return

@json_return
def create(request):
    if request.method != 'POST':
        return HttpResponse(status=403)

    try:
        account_id = int(request.POST['account_id'])
        server_id = int(request.POST['server_id'])
        name = request.POST['name']
    except (KeyError, ValueError):
        res = {
            'ret': 1,
            'msg': 'Invalid request date'
        }
        return res

    if len(name) > 7:
        res = {
            'ret': 20,
            'msg': 'Character Create. name too long'
        }
        return res

    try:
        char = Character.objects.create(
            account_id=account_id,
            server_id=server_id,
            name=name,
        )
    except IntegrityError as e:
        if 'account_id' in e.args[1]:
            res = {
                'ret': 21,
                'msg': 'Character Create. Already have char in this server'
            }
        else:
            res = {
                'ret': 22,
                'msg': 'Character Crate. Duplicate name in server'
            }

        return res

    res = {
        'ret': 0,
        'data': {
            'char_id': char.id
        }
    }

    return res

