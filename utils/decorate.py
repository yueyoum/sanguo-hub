# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'

import json
import struct

from django.http import HttpResponse

NUM_FIELD = struct.Struct('>i')

def json_return(func):
    def wrap(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, dict):
            return HttpResponse(json.dumps(res), content_type='application/json')
        return res
    return wrap

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

