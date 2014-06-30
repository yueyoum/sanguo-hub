# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'

from apps.server.models import Server
from apps.character.models import Character

def _make_server_dict(s):
    return {
        'id': s.id,
        'name': s.name,
        'status': s.status,
        'host': s.host,
        'port': s.port,
        'port_https': s.port_https,
    }

def _servers():
    ss = {}
    for s in Server.objects.all():
        ss[s.id] = _make_server_dict(s)
    return ss

SERVERS = _servers()

def _update_server(s):
    SERVERS[s.id] = _make_server_dict(s)


def register_server(data):
    try:
        server_id = int(data['id'])
        name = data['name']
        host = data['host']
        port = int(data['port'])
        port_https = int(data['port_https'])
    except (KeyError, ValueError):
        return {'ret': 1}

    try:
        s = Server.objects.get(id=server_id)
    except Server.DoesNotExist:
        s = Server()
        s.id = server_id

    s.name = name
    s.status = 1
    s.host = host
    s.port = port
    s.port_https = port_https
    s.save()

    _update_server(s)
    return {'ret': 0}


def get_server_list(account_id=None):
    user_servers = []
    if account_id:
        user_servers = Character.objects.only('server_id').filter(
            account_id=account_id).values_list('server_id', flat=True)

    all_servers = []
    servers = SERVERS.items()
    servers.sort(key=lambda item: item[0])

    for sid, s in servers:
        this = {
            'id': sid,
            'name': s['name'],
            'status': s['status'],  # FIXME, update server status
            'host': s['host'],
            'port': s['port'],
            'port_https': s['port_https'],
            'have_char': sid in user_servers
        }

        all_servers.append(this)

    return all_servers


# FIXME
def update_server(data):
    pass
