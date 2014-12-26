# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/2/14'


from apps.account.models import AccountAnonymous, AccountRegular, AccountThird

from core.server import get_server_list
from core.account import check_allowed_account
from core.exception import GateException
from utils.decorate import proto_return
from libs import pack_msg
from libs.helpers import make_account_dict_from_message
from preset import errormsg

from protomsg import GetServerListResponse


def _msg_server(msg, s):
    msg.id = s['id']
    msg.name = s['name']
    msg.status = s['status']
    msg.have_char = s['have_char']
    msg.host = "http://%s" % s['host']
    msg.port = s['port']


@proto_return
def server_list(request):
    req = request._proto

    try:
        account_data = make_account_dict_from_message(req.login)
    except Exception as e:
        print e

        msg = GetServerListResponse()
        msg.ret = errormsg.BAD_MESSAGE
        return pack_msg(msg)

    try:
        check_allowed_account(account_data)
    except GateException:
        msg = GetServerListResponse()
        msg.ret = errormsg.INVALID_OPERATE
        return pack_msg(msg)

    if account_data['method'] == 'anonymous':
        try:
            acc = AccountAnonymous.objects.select_related('account').get(id=account_data['token'])
        except AccountAnonymous.DoesNotExist:
            acc = None
    elif account_data['method'] == 'regular':
        try:
            acc = AccountRegular.objects.select_related('account').get(name=account_data['name'])
            if acc.passwd != account_data['password']:
                acc = None
        except AccountRegular.DoesNotExist:
            acc = None
    elif account_data['method'] == 'third':
        try:
            acc = AccountThird.objects.select_related('account').get(platform=account_data['platform'], uid=account_data['uid'])
        except AccountThird.DoesNotExist:
            acc = None
    else:
        acc = None

    if acc:
        account_id = acc.account.id
    else:
        account_id = None

    is_test = request.environ.get('NEW_GAME_VERSION', 0) == '1'
    all_servers = get_server_list(account_id=account_id, is_test=is_test)

    top = None
    if acc:
        for s in all_servers:
            if s['id'] == acc.account.last_server_id:
                top = s
                break

    if not top:
        top = all_servers[-1]

    response = GetServerListResponse()
    response.ret = 0

    _msg_server(response.top, top)
    for s in all_servers:
        msg_s = response.servers.add()
        _msg_server(msg_s, s)

    return pack_msg(response)
