# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '2/26/14'

from _base import Logger

import json
import traceback
from itertools import groupby

from django.db.models import Q
from django.utils import timezone


from apps.mail.models import Mail as ModelMail
from apps.character.models import Character
from core.server import make_servers

from utils.api import api_send_mail, APIFailure

#
# API /api/mail/send
# payload
# {
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
    }

    if mail.attachment:
        data['mail']['attachment'] = mail.attachment.export_data()
    else:
        data['mail']['attachment'] = ''
    return data



def send_one_mail(mail, server_ids):
    data = make_payload(mail)

    # data format:
    # {
    #     'char_ids': [],
    #     'mail': {},
    # }

    # 某server收到send_mail的api请求后，如果data中有 char_ids，那么就是发送给这些角色
    # 如果没有char_ids，那么就是发送给全服

    has_send_to = [int(i) for i in mail.has_send_to.split(',') if i.isdigit()]

    if mail.send_type == 3:
        # 发给部分角色
        cids = [int(i) for i in mail.send_to.split(',') if int(i) not in has_send_to]
        chars = Character.objects.filter(id__in=cids)
        cid_sid = [(c.id, c.server_id) for c in chars]
        cid_sid.sort(key=lambda item: item[1])
        cid_sid = groupby(cid_sid, lambda item: item[1])

        for sid, in_server_cids in cid_sid:
            this_server_cids = [_c for _c, _ in in_server_cids]
            data['char_id'] = this_server_cids
            try:
                api_send_mail(sid, json.dumps(data))
            except APIFailure:
                raise Exception("send mail error!")
            else:
                mail.has_send_to = mail.has_send_to + ',' + ','.join([str(i) for i in this_server_cids])
                mail.save()
        return

    if mail.send_type == 1:
        # 发给全部
        sids = server_ids
    else:
        # 发给部分服务器
        sids = [int(i) for i in mail.send_to.split(',') if int(i) not in has_send_to]

    for sid in sids:
        try:
            api_send_mail(sid, json.dumps(data))
        except APIFailure:
            raise Exception("send mail error!")
        else:
            mail.has_send_to = mail.has_send_to + ',' + str(sid)
            mail.save()


def run():
    mails = ModelMail.objects.filter(Q(status=1) & Q(send_at__lte=timezone.now()))
    logger = Logger('send_mail.log')
    logger.write('Send Mail Start. mails amount: {0}'.format(mails.count()))

    servers = make_servers()
    available_server_ids = [k for k, v in servers.items() if v['status'] != 4]

    for m in mails:
        m.status = 2
        m.save()

        logger.write("send {0}...".format(m.id))
        try:
            send_one_mail(m, available_server_ids)
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
