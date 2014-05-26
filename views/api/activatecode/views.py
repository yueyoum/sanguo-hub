# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '5/26/14'

from core.activatecode import use as ac_use
from utils.decorate import json_return

from preset import errormsg

@json_return
def use(request):
    try:
        char_id = int(request.POST['char_id'])
        code_id = request.POST['code_id']
    except:
        return {'ret': errormsg.BAD_MESSAGE}

    return ac_use(char_id, code_id)
