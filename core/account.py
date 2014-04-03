# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/2/14'

from django.db import transaction, IntegrityError

from apps.account.models import AccountAnonymous, AccountRegular, AccountThird, Account
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

    return {'ret': 0, 'account_id': account.account.id}
