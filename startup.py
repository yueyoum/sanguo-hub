# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-10-20'

from django.conf import settings

import requests


def main():
    version = requests.get(settings.VERSION_URL).content.rstrip('\n')
    settings.SERVER_VERSION = version
