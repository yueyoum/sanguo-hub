# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-6-12'

# import json
# import traceback
#
# import uwsgidecorators
#
# from cron.log import Logger
# from core.checkin import get_checkin_obj
# from utils.api import api_send_checkin_data
#
# @uwsgidecorators.cron(0, 0, -1, -1, -1)
# def run(signum):
#     logger = Logger('send_checkin_data.log')
#     logger.write("Send CheckIn Data Start.")
#
#     checkin_obj = get_checkin_obj()
#
#     logger.write("Got CheckIn Object: {0}".format(checkin_obj.checkin_date))
#
#     data = json.dumps(checkin_obj.export_data())
#
#     error_servers = api_send_checkin_data(data)
#     if error_servers:
#         logger.write("ERROR SERVERS: {0}".format(error_servers))
#
#     logger.write("Done")
#     logger.close()
