# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'

from core.account import account_login

from utils.decorate import json_return


@json_return
def login(request):
    return account_login(request.POST)

