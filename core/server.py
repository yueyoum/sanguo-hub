# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'

from django.db import transaction

from apps.server.models import ServerNode, Server
from apps.character.models import Character
from core.exception import GateException


def _nodes():
    nodes = {}
    for n in ServerNode.objects.all():
        nodes[n.id] = {
            'host': n.host,
            'port': n.port,
            'port_https': n.port_https
        }
    return nodes

NODES = _nodes()

def _servers():
    ss = {}
    for s in Server.objects.select_related('node').all():
        ss[s.id] = {
            'name': s.name,
            'host': s.node.host,
            'port': s.node.port,
            'port_https': s.node.port_https,
            'status': s.status,
            'node': s.node.id
        }
    return ss

SERVERS = _servers()



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
            'status': s['status'],  # FIXME, how to get server status
            'host': s['host'],
            'port': s['port'],
            'port_https': s['port_https'],
            'have_char': sid in user_servers
        }

        all_servers.append(this)

    return all_servers


# FIXME
def update_servers(data):
    pass
