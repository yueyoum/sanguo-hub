# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-6-12'

import json
import traceback

from _base import Logger
from core.checkin import get_checkin_obj
from utils.api import api_send_checkin_data, APIFailure


def run():
    logger = Logger('send_checkin_data.log')
    logger.write("Send CheckIn Data Start.")

    checkin_obj = get_checkin_obj()

    logger.write("Got CheckIn Object: {0}".format(checkin_obj.checkin_date))

    data = json.dumps(checkin_obj.export_data())

    try:
        api_send_checkin_data(data)
    except APIFailure:
        logger.write("---- APIFailure ----")
        logger.write(traceback.format_exc())

    logger.close()

if __name__ == '__main__':
    run()
