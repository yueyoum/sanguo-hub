# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-6-12'

from _base import Logger

from apps.production.models import StoreProduction


def run():
    logger = Logger('store_refresh_tag_one_goods.log')
    StoreProduction.make_random_tag_one()

    logger.write("refresh complete!")
    logger.close()

if __name__ == '__main__':
    run()
