# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/2/14'

from core.account import account_register
from libs import pack_msg
from utils.decorate import proto_return

from protomsg import RegisterResponse

@proto_return
def register(request):
    req = request._proto

    # FIXME
    data = {
        'method': 'regular',
        'name': req.email,
        'password': req.password,
    }

    res = account_register(data)
    response = RegisterResponse()
    response.ret = res['ret']

    if res['ret'] == 0:
        response.email = req.email
        response.password = req.password

    return pack_msg(response)

