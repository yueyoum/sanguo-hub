# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'


from core.server import register_server
from utils.decorate import json_return

@json_return
def server_register_view(request):
    return register_server(request.POST)
