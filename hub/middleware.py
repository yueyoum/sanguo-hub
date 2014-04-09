# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/2/14'

import struct
from django.http import HttpResponse

import requests

from core.globleobject import SERVERS
from utils import crypto

import protomsg
from protomsg import REQUEST_TYPE, TYPE_COMMAND

NUM_FIELD = struct.Struct('>i')
METHOD_POST = 'POST'
GATE_MSG_TYPE = set([102, 105])
EMPTY_SESSION_MSG_TYPE = set([100, 102, 105])


def _unpack(res):
    msg_id = NUM_FIELD.unpack(res[:4])[0]
    res = res[4:]
    len_of_msg = NUM_FIELD.unpack(res[:4])[0]
    res = res[4:]
    return msg_id, res[:len_of_msg], res[len_of_msg:]


class UnpackAndVerifyData(object):
    def process_request(self, request):
        if request.method != METHOD_POST:
            return HttpResponse(status=403)

        if request.path.startswith('/api/'):
            return None

        data = request.body
        body = data

        num_of_msgs = NUM_FIELD.unpack(data[:4])[0]
        data = data[4:]

        for i in range(num_of_msgs):
            msg_id, msg, data = _unpack(data)
            if msg_id == 51:
                # TODO Check Version
                pass
            else:
                msg_name = REQUEST_TYPE[msg_id]
                proto = getattr(protomsg, msg_name)
                p = proto()
                p.ParseFromString(msg)

                print p

                if msg_id in GATE_MSG_TYPE:
                    request._proto = p
                    return None

                decrypted_session = ""
                if msg_id not in EMPTY_SESSION_MSG_TYPE:
                    try:
                        decrypted_session = crypto.decrypt(p.session)
                    except crypto.BadEncryptedText:
                        print "BAD SESSION"
                        return HttpResponse(status=403)

                if msg_id == 200:
                    # 200 is CreateCharacterRequest
                    server_id = 0
                elif msg_id == 100 or msg_id == 63:
                    # 100 is StartGameRequest
                    # 63  is ResumeRequest
                    server_id = p.server_id
                else:
                    decrypted_session = decrypted_session.split(':')
                    server_id = int(decrypted_session[1])

                # TODO check server_id
                url, port = SERVERS[server_id]['url'], SERVERS[server_id]['port']

                print "route to", url, port

                x = requests.post('{0}:{1}{2}'.format(url, port, TYPE_COMMAND[msg_id]), data=body)
                if not x.ok:
                    raise Exception("requests error!")
                return HttpResponse(x.content, content_type='text/plain')

