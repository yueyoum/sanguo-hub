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



def pong_from_server(server_id, status):
    s = Server.objects.get(id=server_id)
    s.status = status
    s.save()
    _update_server(s)



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
        s = Server.objects.create(
            id=server_id,
            name=name,
            host=host,
            port=port,
            port_https=port_https
        )
        _update_server(s)
        return {'ret': 0}

    if s.host != host:
        print "server {0} try to register. but {0} already exists, and the host {1} not equal the try register host {2}".format(
            server_id, s.host, host
        )
        return {'ret': 2}

    s.name = name
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
