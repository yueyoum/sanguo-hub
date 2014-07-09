# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-6-12'

from _base import Logger
from utils.api import api_check_server
from core.server import make_servers, pong_from_server


def run():
    logger = Logger('check_server.log')
    servers = make_servers()

    for s in servers.keys():
        try:
            res = api_check_server(s)
        except:
            import traceback
            logger.write('---- ERROR ----')
            logger.write(traceback.format_exc())
            status = 4
            active_amount = None
        else:
            status = res['data']['status']
            active_amount = res['data']['active_amount']

        pong_from_server(s, status, active_amount)
        logger.write("server {0} status {1}".format(s, status))

    logger.write("server check complete!")
    logger.close()


if __name__ == '__main__':
    run()
