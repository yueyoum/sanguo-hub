# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'

import logging

logger = logging.getLogger('gate')

class GateException(Exception):
    def __init__(self, error_id, error_msg=""):
        self.error_id = error_id
        self.error_msg = error_msg
        if error_msg:
            logger.info("[EXCEPTION {0}] {1}".format(error_id, error_msg))
        Exception.__init__(self)


class APIDataError(Exception):
    pass

