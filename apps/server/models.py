from django.db import models
from django.db.models.signals import post_save, post_delete


class Server(models.Model):
    STATUS = (
        (1, 'GOOD'), (2, 'BUSY'), (3, 'NEW'), (4, 'DOWN')
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=32)

    status = models.IntegerField(choices=STATUS, default=1)

    host = models.CharField(max_length=255)
    port = models.IntegerField()
    port_https = models.IntegerField()

    active_players = models.IntegerField(default=0)

    class Meta:
        db_table = 'server'
        ordering = ('id',)


def _change_handler(*args, **kwargs):
    from core.server import make_servers
    make_servers()

post_save.connect(
    _change_handler,
    sender=Server,
    dispatch_uid='apps.server.post_save'
)

post_delete.connect(
    _change_handler,
    sender=Server,
    dispatch_uid='apps.server.post_delete'
)


