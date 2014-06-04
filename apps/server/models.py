from django.db import models


class ServerNode(models.Model):
    id = models.IntegerField(primary_key=True)
    host = models.CharField(max_length=255)
    port = models.IntegerField()
    port_https = models.IntegerField()

    class Meta:
        db_table = 'server_node'
        ordering = ('id',)


class Server(models.Model):
    STATUS = (
        (1, 'GOOD'), (2, 'BUSY'), (3, 'FULL'), (4, 'DOWN')
    )

    id = models.IntegerField(primary_key=True)
    node = models.ForeignKey(ServerNode, related_name='servers')
    name = models.CharField(unique=True, max_length=32)
    status = models.IntegerField(choices=STATUS)

    class Meta:
        db_table = 'server'
