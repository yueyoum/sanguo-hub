# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-7-21'

import json

from django.http import HttpResponse
from apps.broadcast.models import Broadcast

def get_broadcast(request):
    broadcasts = Broadcast.objects.filter(display=True).order_by('-id')
    data = []

    for cast in broadcasts:
        data.append({
            'title': cast.title,
            'image': cast.image,
            'content': cast.content,
            'link': cast.link,
            'date': cast.create_at,
        })

    return HttpResponse(json.dumps(data), content_type='application/json')
