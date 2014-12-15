# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-6-12'

import uwsgidecorators

from cron.log import Logger

from apps.production.models import StoreProduction

@uwsgidecorators.cron(0, -1, -1, -1, -1)
def run(signum):
    logger = Logger('store_refresh_tag_one_goods.log')
    StoreProduction.make_random_tag_one()

    logger.write("refresh complete!")
    logger.close()

