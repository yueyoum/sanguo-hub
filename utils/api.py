# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '5/29/14'

# Keep APIFailure here
from libs.apiclient import HTTPSAPIClient, APIFailure

from core.server import SERVERS, NODES

HTTPSAPIClient.install_pem('/opt/ca/client.pem')
apicall = HTTPSAPIClient()

def api_character_initialize(server_id, data):
    s = SERVERS[server_id]
    url = 'https://{0}:{1}/api/character/initialize/'.format(s['host'], s['port_https'])
    return apicall(data=data, cmd=url)

def api_purchase_done(server_id, data):
    s = SERVERS[server_id]
    url = 'https://{0}:{1}/api/purchase/done/'.format(s['host'], s['port_https'])
    return apicall(data=data, cmd=url)

def api_send_mail(server_id, data):
    s = SERVERS[server_id]
    url = 'https://{0}:{1}/api/mail/send/'.format(s['host'], s['port_https'])
    return apicall(data=data, cmd=url)

def api_send_checkin_data(data):
    for n in NODES.values():
        url = 'https://{0}:{1}/api/checkin/send/'.format(n['host'], n['port_https'])
        apicall(data=data, cmd=url)
