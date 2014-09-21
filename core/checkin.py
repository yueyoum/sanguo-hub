# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-6-12'

from django.conf import settings

import arrow
from apps.checkin.models import CheckInDate


def get_checkin_obj():
    now_date = arrow.utcnow().to(settings.TIME_ZONE).date()
    checkins = CheckInDate.objects.order_by('-checkin_date').filter(checkin_date__lte=now_date)[0:1]
    if checkins:
        checkin_obj = checkins[0]
    else:
        checkins = CheckInDate.objects.all().order_by('-checkin_date')[0:1]
        checkin_obj = checkins[0]

    return checkin_obj
