# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/2/14'

# FIXME
from apps.server.models import Server

def _load_all_servers():
    servers = Server.objects.select_related('node').all()

    res = {}
    for s in servers:
        res[s.id] = {
            'name': s.name,
            'status': s.status,
            'url': s.node.url,
            'port': s.node.port,
        }

    return res

SERVERS = _load_all_servers()
