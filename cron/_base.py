__author__ = 'wang'

import os
import sys
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hub.settings_admin')

from django.conf import settings
from django.utils import timezone
import pytz

LOG_PATH = settings.LOG_PATH


class Logger(object):
    def __init__(self, name):
        self.f = open(os.path.join(LOG_PATH, name), 'a')

    def write(self, text):
        now = timezone.now().replace(tzinfo=pytz.utc).astimezone(pytz.timezone(settings.TIME_ZONE)).strftime("%Y-%m-%d %H:%M:%S")
        self.f.write("{0} {1}\n".format(now, text))

    def close(self):
        self.f.close()
