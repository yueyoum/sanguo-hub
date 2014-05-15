# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '2/26/14'

from _base import Logger

import json
import traceback
from itertools import groupby

from django.db.models import Q
from django.utils import timezone

import requests

from apps.mail.models import Mail as ModelMail
from apps.character.models import Character
from core.server import SERVERS

#
# API /api/mail/send
# payload
# {
#     'server_id': sid,
#     'char_id': [cid, cid...],
#     'mail': {
#         'name': mail name,
#         'content': mail content,
#         'send_at': mail send at,
#         'attachment': {
#             'gold': 0,
#             'sycee': 0,
#             'exp': 0,
#             'official_exp': 0,
#             'heros': [],
#             'souls': [],
#             'equipments': [],
#             'gems': [],
#             'stuffs': []
#         }
#     }
# }
#

def make_payload(mail):
    data = {}
    data['mail'] = {
        'name': mail.name,
        'content': mail.content,
        'send_at': mail.send_at.strftime('%Y-%m-%m %H:%M:%S'),
        'attachment': mail.attachment.export_data()
    }
    return data



def send_one_mail(mail):
    data = make_payload(mail)

    if mail.send_type == 3:
        # 发给部分角色
        cids = [int(i) for i in mail.send_to.split(',')]
        chars = Character.objects.filter(id__in=cids)
        cid_sid = [(c.id, c.server_id) for c in chars]
        cid_sid.sort(key=lambda item: item[1])
        cid_sid = groupby(cid_sid, lambda item: item[1])

        for sid, csids in cid_sid:
            this_server = SERVERS[sid]
            this_server_cids = [_c for _c, _ in csids]
            data['char_id'] = this_server_cids
            req = requests.post('{0}:{1}/api/mail/send/'.format(this_server['url'], this_server['port']), data=json.dumps(data))
            if not req.ok:
                raise Exception("send mail error!")
        return

    if mail.send_type == 1:
        # 发给全部
        sids = SERVERS.keys()
    else:
        # 发给部分服务器
        sids = [int(i) for i in mail.send_to.split(',')]


    for sid in sids:
        data['server_id'] = sid
        this_server = SERVERS[sid]

        req = requests.post('{0}:{1}/api/mail/send/'.format(this_server['url'], this_server['port']), data=json.dumps(data))
        if not req.ok:
            raise Exception("send mail error!")


def run():
    mails = ModelMail.objects.filter(Q(status=1) & Q(send_at__lte=timezone.now()))
    logger = Logger('send_mail.log')
    logger.write('Send Mail Start. mails amount: {0}'.format(mails.count()))

    for m in mails:
        m.status = 2
        m.save()

        logger.write("send {0}...".format(m.id))
        try:
            send_one_mail(m)
        except Exception as e:
            logger.write("ERROR: mail: {0}. error: {1}".format(m.id, str(e)))
            logger.write(traceback.format_exc())
            m.status = 1
        else:
            m.status = 3

        m.save()

    logger.write("Send Mail Complete")
    logger.close()


if __name__ == '__main__':
    run()
