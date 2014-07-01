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
