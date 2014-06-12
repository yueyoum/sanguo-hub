# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-6-12'

from libs.decorate import json_return
from core.checkin import get_checkin_obj

@json_return
def get_checkin_package(request):
    checkin_obj = get_checkin_obj()
    return {
        'ret': 0,
        'data': {
            'checkin': checkin_obj.export_data()
        }
    }

