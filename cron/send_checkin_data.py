# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-6-12'

from _base import Logger

import json
import traceback

import arrow

from apps.checkin.models import CheckInDate
from core.signals import send_checkin_data_signal

from utils.api import api_send_checkin_data, APIFailure


def run(method='SIGNAL'):
    logger = Logger('send_checkin_data.log')
    logger.write("Send CheckIn Data Start By {0}.".format(method))

    checkins = CheckInDate.objects.filter(checkin_date__gte=arrow.utcnow().date())[0:1]
    if checkins:
        checkin_obj = checkins[0]
    else:
        checkins = CheckInDate.objects.all().order_by('-checkin_date')[0:1]
        checkin_obj = checkins[0]

    logger.write("Got CheckIn Object: {0}".format(checkin_obj.checkin_date))

    data = json.dumps(checkin_obj.export_data())

    try:
        api_send_checkin_data(data)
    except APIFailure:
        logger.write("---- APIFailure ----")
        logger.write(traceback.format_exc())

    logger.close()


send_checkin_data_signal.connect(
    run,
    dispatch_uid='cron.send_checkin_data'
)


if __name__ == '__main__':
    run(method='CRON')

