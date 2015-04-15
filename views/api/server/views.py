# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'


from core.server import server_register, get_server_list
from utils.decorate import json_return

@json_return
def server_register_view(request):
    return server_register(request.POST)

@json_return
def server_list(request):
    servers = get_server_list()
    return {
        'ret': 0,
        'data': servers,
    }
