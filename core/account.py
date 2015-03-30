# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/2/14'

import traceback
import hashlib
import requests

from django.conf import settings
from django.db import transaction, IntegrityError

from apps.account.models import AccountAnonymous, AccountRegular, AccountThird, Account
from apps.character.models import Character
from core.exception import GateException
from core.server import make_servers
from preset import errormsg

def check_allowed_account(data):
    allowed_accounts = settings.ALLOWED_ACCOUNTS
    method = data['method']

    if method == 'noaccount' or method == 'anonymous' or method == 'regular':
        if 'self' not in allowed_accounts:
            raise GateException(1)

    if method == 'third':
        if data['platform'] not in allowed_accounts:
                raise GateException(1)


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
    if method == 'noaccount':
        return {
            'method': method,
            'server_id': int(post['server_id']),
        }

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
            'param': post['param'],
            'server_id': int(post['server_id']),

        }

    raise GateException(1)



def account_register(data):
    try:
        data = get_register_request_data(data)
    except (KeyError, GateException):
        return {'ret': errormsg.BAD_MESSAGE}

    try:
        check_allowed_account(data)
    except GateException:
        return {'ret': errormsg.INVALID_OPERATE}

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

    try:
        check_allowed_account(data)
    except GateException:
        return {'ret': errormsg.INVALID_OPERATE}

    servers = make_servers()
    if data['server_id'] not in servers:
        return {'ret': errormsg.SERVER_NOT_EXIST}

    new_token = 0
    if data['method'] == 'noaccount':
        # 建立游客帐号
        try:
            with transaction.atomic():
                account = AccountAnonymous.objects.create()
                new_token = account.id
        except IntegrityError:
            return {'ret': errormsg.ACCOUNT_LOGIN_FAILURE}

    elif data['method'] == 'anonymous':
        # 游客登录
        try:
            account = AccountAnonymous.objects.select_related('account').get(id=data['token'])
        except AccountAnonymous.DoesNotExist:
            return {'ret': errormsg.ACCOUNT_NOT_EXSIT}

    elif data['method'] == 'regular':
        # 自有帐号登录
        try:
            account = AccountRegular.objects.select_related('account').get(name=data['name'])
        except AccountRegular.DoesNotExist:
            return {'ret': errormsg.ACCOUNT_NOT_EXSIT}

        if account.passwd != data['password']:
            return {'ret': errormsg.WRONG_PASSWORD}

    else:
        # 第三方帐号登录
        if data['platform'] == '91':
            try:
                verify_91(data['uid'], data['param'])
            except:
                traceback.print_exc()
                return {'ret': errormsg.ACCOUNT_LOGIN_FAILURE}
        elif data['platform'] == 'jodoplay':
            try:
                verify_jodoplay(data['uid'], data['param'])
            except:
                traceback.print_exc()
                return {'ret': errormsg.ACCOUNT_LOGIN_FAILURE}

        try:
            account = AccountThird.objects.select_related('account').get(platform=data['platform'], uid=data['uid'])
        except AccountThird.DoesNotExist:
            try:
                with transaction.atomic():
                    account = AccountThird.objects.create(platform=data['platform'], uid=data['uid'])
            except IntegrityError:
                return {'ret': errormsg.ACCOUNT_LOGIN_FAILURE}

    # TODO account ban

    account.account.last_server_id = data['server_id']
    account.account.save()

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


def account_find(name):
    ret = {'ret': 0, 'data': {}}

    try:
        account = AccountRegular.objects.get(name=name)
    except AccountRegular.DoesNotExist:
        ret['ret'] = 1
        return ret

    chars = Character.objects.filter(account_id=account.account.id)

    result = []
    for c in chars:
        result.append({
            'char_id': c.id,
            'server_id': c.server_id,
            'name': c.name
        })

    ret['data']['chars'] = result
    return ret





def verify_91(uid, sessionid):
    settings_91 = settings.THIRD_PLATFORM['91']
    url = settings_91['verify']
    appid = settings_91['appid']
    appkey = settings_91['appkey']

    sign_original = "{0}{1}{2}{3}{4}".format(appid, 4, uid, sessionid, appkey)
    sign = hashlib.md5(sign_original).hexdigest()

    data = {
        'Appid': appid,
        'Act': 4,
        'Uin': uid,
        'SessionId': sessionid,
        'Sign': sign
    }

    try:
        res = requests.get(url, data=data)
    except:
        raise GateException(errormsg.ACCOUNT_LOGIN_FAILURE)

    res = res.json()
    print res
    if res['ErrorCode'] != '1':
        raise GateException(errormsg.ACCOUNT_LOGIN_FAILURE)


def verify_jodoplay(uid, sessionid):
    settings_jodoplay = settings.THIRD_PLATFORM['jodoplay']
    url = settings_jodoplay['verify']
    cpid = settings_jodoplay['cpid']
    gameid = settings_jodoplay['gameid']
    channelid = settings_jodoplay['channelid']
    pn = settings_jodoplay['pn']
    secretkey = settings_jodoplay["secretkey"]

    psw_text = "{0}{1}{2}{3}{4}{5}{6}".format(
        secretkey, cpid, gameid, channelid, pn, sessionid, uid
    )

    psw = hashlib.sha256(psw_text).hexdigest()

    data = {
        'cpid': cpid,
        'gameid': gameid,
        'channelid': channelid,
        'pn': pn,
        'sessiontoken': sessionid,
        'gameuid': uid,
        'psw': psw
    }

    try:
        req = requests.get(url, params=data)
    except Exception as e:
        print "==== ERROR ===="
        print "jodoplay verify reqeusts error"
        print e
        raise GateException(errormsg.ACCOUNT_LOGIN_FAILURE)

    res = req.json()
    print res
    if res['state']['code'] != 0:
        raise GateException(errormsg.ACCOUNT_LOGIN_FAILURE)
