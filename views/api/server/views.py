# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'


from core.server import update_servers, SERVERS
from utils.decorate import json_return

@json_return
def server_list(request):
    return {
        'ret': 0,
        'data': SERVERS
    }


@json_return
def server_list_report(request):
    # TODO
    return {
        'ret': 0,
        'data': {}
    }


