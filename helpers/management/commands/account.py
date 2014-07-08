# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-7-8'

from optparse import make_option
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = """Account stuffs. args:
    find --name=<ARG>  find account by name
    """

    option_list = BaseCommand.option_list + (
        make_option('--name',
                    dest='account_name'
                    ),
    )

    def _cmd_error(self):
        self.stdout.write(self.help)

    def handle(self, *args, **options):
        if not args:
            return self._cmd_error()

        if args[0] == 'find':
            account_name = options['account_name']
            if not account_name:
                return self._cmd_error()
            return self._cmd_find(account_name)
        else:
            return self._cmd_error()

    def _cmd_find(self, name):
        from core.account import account_find
        res = account_find(name)
        if res['ret'] != 0:
            self.stdout.write("NOT found, {0}".format(name))
            return

        self.stdout.write("Found {0}. Chars:".format(name))
        for c in res['data']['chars']:
            self.stdout.write(str(c))
