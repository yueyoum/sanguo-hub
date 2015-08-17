# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '5/29/14'

# Keep APIFailure here
from libs.apiclient import HTTPSAPIClient, APIFailure

from core.server import make_servers

HTTPSAPIClient.install_pem('/opt/ca/client.pem')
apicall = HTTPSAPIClient()

def api_character_initialize(server_id, data):
    s = make_servers()[server_id]
    url = u'https://{0}:{1}/api/character/initialize/'.format(s['host'], s['port_https'])
    return apicall(data=data, cmd=url)

def api_character_information(server_id, char_id):
    # 获取角色基本信息
    s = make_servers()[server_id]
    data = {'char_id': char_id}
    url = u'https://{0}:{1}/api/character/information/'.format(s['host'], s['port_https'])
    return apicall(data=data, cmd=url)

def api_character_modify(server_id, char_id, name, value):
    # 获取角色基本信息
    s = make_servers()[server_id]
    data = {'char_id': char_id, 'name': name, 'value': value}

    url = u'https://{0}:{1}/api/character/modify/'.format(s['host'], s['port_https'])
    return apicall(data=data, cmd=url)


def api_character_union(server_id, char_id):
    # 获取角色工会信息
    s = make_servers()[server_id]
    data = {'char_id': char_id}
    url = u'https://{0}:{1}/api/character/union/'.format(s['host'], s['port_https'])
    return apicall(data=data, cmd=url)

def api_send_mail(server_id, data):
    s = make_servers()[server_id]
    url = u'https://{0}:{1}/api/mail/send/'.format(s['host'], s['port_https'])
    return apicall(data=data, cmd=url)

def api_send_checkin_data(data):
    error_servers = []
    for s in make_servers().values():
        url = u'https://{0}:{1}/api/checkin/send/'.format(s['host'], s['port_https'])
        try:
            apicall(data=data, cmd=url)
        except:
            error_servers.append(s['id'])

    return error_servers


def api_check_server(server_id):
    s = make_servers()[server_id]
    url = u'https://{0}:{1}/api/ping/'.format(s['host'], s['port_https'])
    return apicall(data={}, cmd=url)

def api_server_change_feedback(server_id, status):
    s = make_servers()[server_id]
    url = u'https://{0}:{1}/api/server/feedback/'.format(s['host'], s['port_https'])
    apicall(data={'status': status}, cmd=url)


def api_purchase91_done(server_id, char_id, goods_id):
    s = make_servers()[server_id]
    data = {
        'char_id': char_id,
        'goods_id': goods_id,
    }

    url = u'https://{0}:{1}/api/purchase/91/done/'.format(s['host'], s['port_https'])
    apicall(data=data, cmd=url)

def api_purchase_aiyingyong_done(server_id, char_id, goods_id):
    s = make_servers()[server_id]
    data = {
        'char_id': char_id,
        'goods_id': goods_id
    }

    url = u'https://{0}:{1}/api/purchase/aiyingyong/done/'.format(s['host'], s['port_https'])
    apicall(data=data, cmd=url)

def api_purchase_jodoplay_done(server_id, char_id, goods_id, price):
    s = make_servers()[server_id]
    data = {
        'char_id': char_id,
        'goods_id': goods_id,
        'price': price,
    }

    url = u'https://{0}:{1}/api/purchase/jodoplay/done/'.format(s['host'], s['port_https'])
    apicall(data=data, cmd=url)
