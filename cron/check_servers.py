# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-6-12'

import uwsgidecorators
from django.db import connection

from cron.log import Logger
from utils.api import api_check_server
from core.server import make_servers, pong_from_server

@uwsgidecorators.timer(300)
def run(signum):
    connection.close()
    logger = Logger('check_server.log')
    servers = make_servers()

    for s in servers.keys():
        try:
            res = api_check_server(s)
        except:
            import traceback
            logger.write('---- ERROR ----')
            logger.write(traceback.format_exc())
            active_amount = 0
        else:
            active_amount = res['data']['active_amount']

        pong_from_server(s, active_amount)
        logger.write("server {0} active amount {1}".format(s, active_amount))

    logger.write("server check complete!")
    logger.close()
