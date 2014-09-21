# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-9-21'

import arrow
from django.conf import settings
from django.db.models import Q

from libs.decorate import json_return
from apps.system.models import Broadcast

@json_return
def get_system_broadcast(request):
    now_date = arrow.utcnow().to(settings.TIME_ZONE).date()
    casts = Broadcast.objects.filter(
        Q(active=True) & Q(start_at__lte=now_date) & Q(end_at__gte=now_date)
    )

    result = []
    for c in casts:
        result.append({
            'content': c.content,
            'play_times': c.play_times,
        })

    return {
        'ret': 0,
        'data': result
    }

