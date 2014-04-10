# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'

import json

from core.server import get_server_list, update_servers, _servers
from utils.decorate import json_return

@json_return
def server_list(request):
    # all_servers = get_server_list()
    # res = {}
    # for s in all_servers:
    #     res[s['id']] = {
    #         'name': s['name'],
    #         'url': s['url'],
    #         'port': s['port'],
    #         'status': s['status'],
    #     }
    all_servers = _servers()

    return {
        'ret': 0,
        'data': all_servers
    }


@json_return
def server_list_report(request):
    # TODO
    return {
        'ret': 0,
        'data': {}
    }


