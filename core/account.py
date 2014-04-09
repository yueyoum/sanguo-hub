# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/2/14'

from django.db import transaction, IntegrityError

from apps.account.models import AccountAnonymous, AccountRegular, AccountThird, Account
from apps.character.models import Character
from core.exception import GateException


def get_register_request_data(post):
    method = post['method']
    if method == 'regular':
        return {
            'method': method,
            'name': post['name'],
            'password': post['password'],
            'token': post['token'],
        }

    if method == 'third':
        return {
            'method': method,
            'platform': post['platform'],
            'uid': post['uid']
        }

    raise GateException(1)



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



def account_register(data):
    try:
        data = get_register_request_data(data)
    except (KeyError, GateException):
        return {'ret': 1}

    try:
        with transaction.atomic():
            if data['method'] == 'regular':
                try:
                    old_account = AccountAnonymous.objects.get(token=data['token'])
                    print "got old_account"
                except AccountAnonymous.DoesNotExist:
                    account = AccountRegular.objects.create(name=data['name'], passwd=data['password'])
                    print "create regular"
                else:
                    print "xxx"
                    account = AccountRegular.objects.create(name=data['name'], passwd=data['password'], account_id=old_account.account_id)
                    Account.objects.filter(id=old_account.account_id).update(tp='regular')
                    AccountAnonymous.objects.filter(token=data['token']).delete()
            else:
                account = AccountThird.objects.create(platform=data['platform'], uid=data['uid'])
    except IntegrityError:
        return {'ret': 100}

    return {
        'ret': 0,
        'data': {
            'account_id': account.account.id
        }
    }



def account_login(data):
    try:
        data = get_login_request_data(data)
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

