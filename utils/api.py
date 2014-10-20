# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '5/29/14'

# Keep APIFailure here
from libs.apiclient import HTTPSAPIClient, APIFailure

from core.server import SERVERS

HTTPSAPIClient.install_pem('/opt/ca/client.pem')
apicall = HTTPSAPIClient()

def api_character_initialize(server_id, data):
    s = SERVERS[server_id]
    url = u'https://{0}:{1}/api/character/initialize/'.format(s['host'], s['port_https'])
    return apicall(data=data, cmd=url)

def api_send_mail(server_id, data):
    s = SERVERS[server_id]
    url = u'https://{0}:{1}/api/mail/send/'.format(s['host'], s['port_https'])
    return apicall(data=data, cmd=url)

def api_send_checkin_data(data):
    for s in SERVERS.values():
        url = u'https://{0}:{1}/api/checkin/send/'.format(s['host'], s['port_https'])
        apicall(data=data, cmd=url)


def api_check_server(server_id):
    s = SERVERS[server_id]
    url = u'https://{0}:{1}/api/ping/'.format(s['host'], s['port_https'])
    return apicall(data={}, cmd=url)

def api_server_change_feedback(server_id, status):
    s = SERVERS[server_id]
    url = u'https://{0}:{1}/api/server/feedback/'.format(s['host'], s['port_https'])
    apicall(data={'status': status}, cmd=url)


def api_purchase91_done(server_id, char_id, goods_id):
    s = SERVERS[server_id]
    data = {
        'char_id': char_id,
        'goods_id': goods_id,
    }

    url = u'https://{0}:{1}/api/purchase91/done/'.format(s['host'], s['port_https'])
    apicall(data=data, cmd=url)

def api_server_version_change(version):
    for index, s in enumerate(SERVERS.values()):
        data = {
            'version': version,
            'index': index
        }
        url = u'https://{0}:{1}/api/server/version/'.format(s['host'], s['port_https'])
        apicall(data=data, cmd=url)
