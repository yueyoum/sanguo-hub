# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'

import struct
from django.http import HttpResponse

from libs.decorate import json_return

NUM_FIELD = struct.Struct('>i')


def proto_return(func):
    def wrap(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, (list, tuple)):
            num_of_msgs = len(res)
            res = ''.join(res)
        else:
            num_of_msgs = 1

        data = '%s%s' % (
            NUM_FIELD.pack(num_of_msgs),
            res
        )

        return HttpResponse(data, content_type='text/plain')
    return wrap

