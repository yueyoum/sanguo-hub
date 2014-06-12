# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-6-12'

from libs.decorate import json_return
from core.signals import send_checkin_data_signal

@json_return
def get_checkin_package(request):
    send_checkin_data_signal.send(sender=None)
    return {'ret': 0}
