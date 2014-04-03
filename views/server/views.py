# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/2/14'


from apps.account.models import AccountAnonymous, AccountRegular, AccountThird

from core.server import get_server_list
from utils import pack_msg
from utils.decorate import proto_return

from protomsg import GetServerListResponse


def _msg_server(msg, s):
    msg.id = s['id']
    msg.name = s['name']
    msg.status = s['status']
    msg.have_char = s['have_char']


@proto_return
def server_list(request):
    req = request._proto

    # FIXME
    if req.anonymous.device_token:
        try:
            acc = AccountAnonymous.objects.select_related('account').get(token=req.anonymous.device_token)
        except AccountAnonymous.DoesNotExist:
            acc = None
    else:
        try:
            acc = AccountRegular.objects.select_related('account').get(name=req.regular.email)
            if acc.passwd != req.regular.password:
                acc = None
        except AccountRegular.DoesNotExist:
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
        top = all_servers[-1]

    print top
    print all_servers

    response = GetServerListResponse()
    response.ret = 0

    _msg_server(response.top, top)
    for s in all_servers:
        msg_s = response.servers.add()
        _msg_server(msg_s, s)

    return pack_msg(response)

