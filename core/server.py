# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'

from core.version import version
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


def make_servers(is_test=None):
    servers = {}
    if is_test is None:
        queryset = Server.objects.all()
    else:
        queryset = Server.objects.filter(is_test=is_test)

    for s in queryset:
        servers[s.id] = _make_server_dict(s)

    return servers



def pong_from_server(server_id, active_amount=None):
    s = Server.objects.get(id=server_id)
    if active_amount is not None:
        s.active_players = active_amount
    s.save()



def server_register(data):
    return_data = {
        'ret': 0,
        'data': {
            'version': version.version,
        }
    }

    try:
        server_id = int(data['id'])
        name = data['name']
        host = data['host']
        port = int(data['port'])
        port_https = int(data['port_https'])
        is_test = data['is_test'] == '1'
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
            port_https=port_https,
            is_test=is_test
        )
        return return_data

    if s.host != host:
        print "server {0} try to register. but {0} already exists, and the host {1} not equal the try register host {2}".format(
            server_id, s.host, host
        )
        return {'ret': 2}

    s.name = name
    s.port = port
    s.port_https = port_https
    s.is_test = is_test
    s.save()

    return return_data


def get_server_list(account_id=None, is_test=False):
    user_servers = []
    if account_id:
        user_servers = Character.objects.only('server_id').filter(
            account_id=account_id).values_list('server_id', flat=True)

    all_servers = []
    servers = make_servers(is_test=is_test).items()
    servers.sort(key=lambda item: item[0])

    for sid, s in servers:
        this = {
            'id': sid,
            'name': s['name'],
            'status': s['status'],
            'host': s['host'],
            'port': s['port'],
            'port_https': s['port_https'],
            'have_char': sid in user_servers
        }

        all_servers.append(this)

    return all_servers

