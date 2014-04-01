from django.db import models

class Character(models.Model):
    account_id = models.IntegerField()
    server_id = models.IntegerField()
    name = models.CharField(max_length=16)

    class Meta:
        db_table = 'char_'
        unique_together = (
            ('account_id', 'server_id'),
            ('server_id', 'name'),
        )
