from django.db import models


class Server(models.Model):
    STATUS = (
        (1, 'GOOD'), (2, 'BUSY'), (3, 'FULL'), (4, 'DOWN')
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=32)

    status = models.IntegerField(choices=STATUS, default=1)

    host = models.CharField(max_length=255)
    port = models.IntegerField()
    port_https = models.IntegerField()

    players = models.IntegerField(default=0)
    active_players = models.IntegerField(default=0)

    class Meta:
        db_table = 'server'
        ordering = ('id',)
