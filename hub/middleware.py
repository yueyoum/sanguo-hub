# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/2/14'

from django.http import HttpResponse

from libs import (
    NUM_FIELD,
    METHOD_POST,
    msg_unpack,
)


class RequestFilter(object):
    def process_request(self, request):
        if request.method != METHOD_POST:
            return HttpResponse(status=403)

        if request.path.startswith('/api/'):
            return None

        data = request.body

        num_of_msgs = NUM_FIELD.unpack(data[:4])[0]
        data = data[4:]

        for i in range(num_of_msgs):
            msg_id, msg, data = msg_unpack(data)
            if msg_id == 51:
                # TODO Check Version
                pass
            else:
                return None

