# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'


from core.server import update_server, SERVERS, register_server
from utils.decorate import json_return

@json_return
def server_list(request):
    return {
        'ret': 0,
        'data': SERVERS
    }


@json_return
def server_report_view(request):
    # TODO
    return {
        'ret': 0,
        'data': {}
    }


@json_return
def server_register_view(request):
    return register_server(request.POST)
