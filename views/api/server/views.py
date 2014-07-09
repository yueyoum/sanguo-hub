# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'


from core.server import server_register, server_change
from utils.decorate import json_return

@json_return
def server_register_view(request):
    return server_register(request.POST)

@json_return
def server_change_view(request):
    return server_change(request.POST)
