# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'


from django.http import HttpResponse
from django.db import transaction, IntegrityError

from apps.account.models import AccountAnonymous, AccountRegular, AccountThird, Account
from core.exception import GateException

from utils.decorate import json_return


def get_login_request_data(post):
    method = post['method']
    if method == 'anonymous':
        return {
            'method': method,
            'token': post['token']
        }

    if method == 'regular':
        return {
            'method': method,
            'name': post['name'],
            'password': post['password']
        }

    if method == 'third':
        return {
            'method': method,
            'platform': post['platform'],
            'uid': post['uid']
        }

    raise GateException(1)


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


@json_return
def register(request):
    if request.method != 'POST':
        return HttpResponse(status=403)

    try:
        data = get_register_request_data(request.POST)
    except (KeyError, GateException):
        res = {
            'ret': 1,
            'msg': 'Invalid request date'
        }
        return res

    try:
        with transaction.atomic():
            if data['method'] == 'regular':
                try:
                    old_account = AccountAnonymous.objects.get(token=data['token'])
                except AccountAnonymous.DoesNotExist:
                    account = AccountRegular.objects.create(name=data['name'], passwd=data['password'])
                else:
                    account = AccountRegular.objects.create(name=data['name'], passwd=data['password'], account_id=old_account.account_id)
                    Account.objects.filter(id=old_account.account_id).update(tp='regular')
                    AccountAnonymous.objects.filter(token=data['token']).delete()
            else:
                account = AccountThird.objects.create(platform=data['platform'], uid=data['uid'])
    except IntegrityError:
        res = {
            'ret': 2,
            'msg': 'DataBase IntegrityError'
        }
        return res

    res = {
        'ret': 0,
        'data': {
            'account_id': account.account.id
        }
    }
    return res


@json_return
def login(request):
    if request.method != 'POST':
        return HttpResponse(status=403)

    try:
        data = get_login_request_data(request.POST)
    except (KeyError, GateException):
        res = {
            'ret': 1,
            'msg': 'Invalid request date'
        }
        return res

    if data['method'] == 'anonymous':
        # 匿名登录，如果没此记录，就创建用户
        try:
            account = AccountAnonymous.objects.select_related('account').get(token=data['token'])
        except AccountAnonymous.DoesNotExist:
            try:
                with transaction.atomic():
                    account = AccountAnonymous.objects.create(token=data['token'])
            except IntegrityError:
                res = {
                    'ret': 2,
                    'msg': 'DataBase IntegrityError'
                }

                return res

    elif data['method'] == 'regular':
        try:
            account = AccountRegular.objects.select_related('account').get(name=data['name'])
        except AccountRegular.DoesNotExist:
            res = {
                'ret': 3,
                'msg': 'Account Not Exist'
            }
            return res

        if account.passwd != data['password']:
            res = {
                'ret': 4,
                'msg': 'Account Wrong Password'
            }
            return res

    else:
        try:
            account = AccountThird.objects.select_related('account').get(platform=data['platform'], uid=data['uid'])
        except AccountThird.DoesNotExist:
            res = {
                'ret': 3,
                'msg': 'Account Not Exist'
            }
            return res

    res = {
        'ret': 0,
        'data': {
            'account_id': account.account.id
        }
    }
    return res
