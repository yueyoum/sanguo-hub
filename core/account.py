# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/2/14'

from django.db import transaction, IntegrityError

from apps.account.models import AccountAnonymous, AccountRegular, AccountThird, Account
from apps.character.models import Character
from core.exception import GateException
from preset import errormsg


def get_register_request_data(post):
    method = post['method']
    if method == 'regular':
        return {
            'method': method,
            'name': post['name'],
            'password': post['password'],
        }

    if method == 'third':
        return {
            'method': method,
            'platform': post['platform'],
            'uid': post['uid']
        }

    raise GateException(1)


def get_bind_request_data(post):
    data = {
        'name': post['name'],
        'password': post['password'],
        'token': post['token'],
    }

    for v in data.values():
        if not v:
            raise GateException(1)

    return data


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
        return {'ret': errormsg.BAD_MESSAGE}

    try:
        with transaction.atomic():
            if data['method'] == 'regular':
                account = AccountRegular.objects.create(name=data['name'], passwd=data['password'])
            else:
                account = AccountThird.objects.create(platform=data['platform'], uid=data['uid'])
    except IntegrityError:
        return {'ret': errormsg.ACCOUNT_HAS_BEEN_REGISTED}

    return {
        'ret': 0,
        'data': {
            'account_id': account.account.id
        }
    }


def account_bind(data):
    try:
        data = get_bind_request_data(data)
    except (KeyError, GateException):
        return {'ret': errormsg.BAD_MESSAGE}

    try:
        old_account = AccountAnonymous.objects.get(id=int(data['token']))
    except AccountAnonymous.DoesNotExist:
        return {'ret': errormsg.ACCOUNT_NOT_EXSIT}

    try:
        with transaction.atomic():
            new_account = AccountRegular.objects.create(name=data['name'], passwd=data['password'], account_id=old_account.account.id)
            Account.objects.filter(id=old_account.account.id).update(tp='regular')
            old_account.delete()
    except IntegrityError:
        return {'ret': errormsg.ACCOUNT_HAS_BEEN_REGISTED}

    return {
        'ret': 0,
    }



def account_login(data):
    try:
        data = get_login_request_data(data)
    except (KeyError, ValueError, GateException):
        return {'ret': errormsg.BAD_MESSAGE}

    new_token = 0
    if data['method'] == 'anonymous':
        # 匿名登录
        if not data['token']:
            # 建立新的游客帐号
            try:
                with transaction.atomic():
                    account = AccountAnonymous.objects.create()
                    new_token = account.id
            except IntegrityError:
                return {'ret': errormsg.ACCOUNT_LOGIN_FAILURE}
        else:
            try:
                new_token = int(data['token'])
            except:
                return {'ret': errormsg.BAD_MESSAGE}

            try:
                account = AccountAnonymous.objects.select_related('account').get(id=new_token)
            except AccountAnonymous.DoesNotExist:
                return {'ret': errormsg.ACCOUNT_NOT_EXSIT}

    elif data['method'] == 'regular':
        try:
            account = AccountRegular.objects.select_related('account').get(name=data['name'])
        except AccountRegular.DoesNotExist:
            return {'ret': errormsg.ACCOUNT_NOT_EXSIT}

        if account.passwd != data['password']:
            return {'ret': errormsg.WRONG_PASSWORD}

    else:
        try:
            account = AccountThird.objects.select_related('account').get(platform=data['platform'], uid=data['uid'])
        except AccountThird.DoesNotExist:
            try:
                with transaction.atomic():
                    account = AccountThird.objects.create(platform=data['platform'], uid=data['uid'])
            except IntegrityError:
                return {'ret': errormsg.ACCOUNT_LOGIN_FAILURE}

    # TODO account ban
    try:
        char = Character.objects.get(account_id=account.account.id, server_id=data['server_id'])
        char_id = char.id
    except Character.DoesNotExist:
        char_id = 0

    res = {
        'ret': 0,
        'data': {
            'account_id': account.account.id,
            'char_id': char_id,
            'new_token': new_token,
        }
    }
    return res
