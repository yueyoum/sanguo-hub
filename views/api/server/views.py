# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'


from core.server import server_register
from core.version import version
from utils.decorate import json_return

@json_return
def server_register_view(request):
    return server_register(request.POST)


@json_return
def version_back(request):
    version_text = request.POST['version']
    version.set_version(version_text)
    return {'ret': 0}
