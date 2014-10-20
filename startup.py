# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-10-20'

from django.conf import settings

import requests
from core.version import version


def main():
    version_text = requests.get(settings.VERSION_URL).content.rstrip('\n')
    version.set_version(version_text)
