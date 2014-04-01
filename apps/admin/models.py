from django.db import models

class Admin(models.Model):
    name = models.CharField(max_length=64)
    passwd = models.CharField(max_length=64)
    last_login_at = models.DateTimeField()
    last_login_ip = models.CharField(max_length=20)

    can_login = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    # if can_login = True and active = False
    # readonly mode

    class Meta:
        db_table = 'admin'
