# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'

from django.db import transaction

from apps.server.models import ServerNode, Server
from apps.character.models import Character
from core.exception import GateException

def _servers():
    ss = {}
    for s in Server.objects.select_related('node').all():
        ss[s.id] = {
            'name': s.name,
            'url': s.node.url,
            'port': s.node.port,
            'status': s.status,
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
            'url': s['url'],
            'port': s['port'],
            'have_char': sid in user_servers
        }

        all_servers.append(this)

    return all_servers


# FIXME
def update_servers(data):
    try:
        node_id = int(data['node-id'])
        url = data['url']
        port = data['port']

        servers = []
        for s in data['servers']:
            servers.append([int(s['id']), s['name'], int(s['status'])])

    except (KeyError, ValueError):
        raise GateException(1)

    with transaction.atomic():
        try:
            node = ServerNode.objects.get(id=node_id)
        except ServerNode.DoesNotExist:
            node = ServerNode(id=node_id)

        node.url = url
        node.port = port
        node.save()

        node.servers.all().delete()

        server_datas = []
        for _id, name, status in servers:
            server_datas.append(
                Server(node=node, sid=_id, name=name, status=status)
            )

        Server.objects.bulk_create(server_datas)

