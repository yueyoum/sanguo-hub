# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'


from django.http import HttpResponse
from django.db import transaction, IntegrityError

from apps.account.models import AccountAnonymous, AccountRegular, AccountThird, Account
from apps.character.models import Character
from core.exception import GateException

from utils.decorate import json_return


def get_login_request_data(post):
    method = post['method']
    if method == 'anonymous':
        return {
            'method': method,
            'token': post['token'],
            'server_id': int(post['server_id']),
        }

    if method == 'regular':
        return {
            'method': method,
            'name': post['name'],
            'password': post['password'],
            'server_id': int(post['server_id']),

        }

    if method == 'third':
        return {
            'method': method,
            'platform': post['platform'],
            'uid': post['uid'],
            'server_id': int(post['server_id']),

        }

    raise GateException(1)


@json_return
def login(request):
    try:
        data = get_login_request_data(request.POST)
    except (KeyError, ValueError, GateException):
        return {'ret': 1}

    if data['method'] == 'anonymous':
        # 匿名登录，如果没此记录，就创建用户
        try:
            account = AccountAnonymous.objects.select_related('account').get(token=data['token'])
        except AccountAnonymous.DoesNotExist:
            try:
                with transaction.atomic():
                    account = AccountAnonymous.objects.create(token=data['token'])
            except IntegrityError:
                return {'ret': 2}

    elif data['method'] == 'regular':
        try:
            account = AccountRegular.objects.select_related('account').get(name=data['name'])
        except AccountRegular.DoesNotExist:
            return {'ret': 20}

        if account.passwd != data['password']:
            return {'ret': 21}

        # TODO account ban
    else:
        try:
            account = AccountThird.objects.select_related('account').get(platform=data['platform'], uid=data['uid'])
        except AccountThird.DoesNotExist:
            try:
                with transaction.atomic():
                    account = AccountThird.objects.create(platform=data['platform'], uid=data['uid'])
            except IntegrityError:
                return {'ret': 2}

    try:
        char = Character.objects.get(account_id=account.account.id, server_id=data['server_id'])
        char_id = char.id
    except Character.DoesNotExist:
        char_id = 0

    res = {
        'ret': 0,
        'data': {
            'account_id': account.account.id,
            'char_id': char_id
        }
    }
    return res
