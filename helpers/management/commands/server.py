# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-7-8'


from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = """Server stuffs. args:
    status   output servers status.
    """

    def handle(self, *args, **options):
        if not args:
            self.stdout.write(self.help)
            return

        if args[0] == 'status':
            self._cmd_status()
        else:
            self.stdout.write(self.help)
            return

    def _cmd_status(self):
        from core.server import make_servers
        servers = make_servers()
        self.stdout.write("Total {0} servers".format(len(servers)))
        for s in servers.values():
            text = "%3d: host: %s, port: %d, port_https: %d, status: %d, name: %s" % (
                s['id'], s['host'], s['port'], s['port_https'], s['status'], s['name']
            )

            self.stdout.write(text)
