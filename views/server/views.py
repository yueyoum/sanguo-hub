# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/2/14'


from apps.account.models import AccountAnonymous, AccountRegular

from core.server import get_server_list
from utils.decorate import proto_return
from libs import pack_msg
from preset import errormsg

from protomsg import GetServerListResponse


def _msg_server(msg, s):
    msg.id = s['id']
    msg.name = s['name']
    msg.status = s['status']
    msg.have_char = s['have_char']
    msg.host = s['host']
    msg.port = s['port']


@proto_return
def server_list(request):
    req = request._proto

    token = req.anonymous.device_token
    email = req.regular.email
    password = req.regular.password

    if token:
        try:
            token = int(token)
        except:
            x = GetServerListResponse()
            x.ret = errormsg.BAD_MESSAGE
            return pack_msg(x)

        try:
            acc = AccountAnonymous.objects.select_related('account').get(id=int(token))
        except AccountAnonymous.DoesNotExist:
            acc = None
    elif email:
        try:
            acc = AccountRegular.objects.select_related('account').get(name=email)
            if acc.passwd != password:
                acc = None
        except AccountRegular.DoesNotExist:
            acc = None
    else:
        acc = None

    if acc:
        account_id = acc.account.id
    else:
        account_id = None

    all_servers = get_server_list(account_id)

    top = None
    if acc:
        for s in all_servers:
            if s['id'] == acc.account.last_server_id:
                top = s
                break

    if not top:
        top = all_servers[0]

    response = GetServerListResponse()
    response.ret = 0

    _msg_server(response.top, top)
    for s in all_servers:
        msg_s = response.servers.add()
        _msg_server(msg_s, s)

    return pack_msg(response)
