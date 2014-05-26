# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '5/19/14'

"""
All api requests are POST to HTTPS api server
This Lib Only define a apicall method.

Who using this lib, should
"""


import requests


class APIFailure(Exception):
    pass

class APIClient(object):
    def __init__(self, pem):
        self.pem = pem

    def __call__(self, *args, **kwargs):
        pass
