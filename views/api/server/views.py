# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'

import json

from core.server import get_server_list, update_servers
from utils.decorate import json_return


@json_return
def server_list(request):
    if request.method == 'GET':
        account_id = request.GET.get('account_id', 0)

        try:
            account_id = int(account_id)
        except ValueError:
            res = {
                'ret': 1,
                'msg': 'Invalid request date'
            }
            return res

        return get_server_list(account_id)

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except:
            res = {
                'ret': 1,
                'msg': 'Invalid request date'
            }
            return res

        print data

        update_servers(data)

        res = {
            'ret': 0,
        }
        return res
