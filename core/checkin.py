# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-6-12'


import arrow
from apps.checkin.models import CheckInDate


def get_checkin_obj():
    checkins = CheckInDate.objects.filter(checkin_date__gte=arrow.utcnow().date())[0:1]
    if checkins:
        checkin_obj = checkins[0]
    else:
        checkins = CheckInDate.objects.all().order_by('-checkin_date')[0:1]
        checkin_obj = checkins[0]

    return checkin_obj
