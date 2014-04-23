# # -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError

from apps.package.models import Package
from apps.server.models import Server
from apps.character.models import Character


class Mail(models.Model):
    STAUTS = (
        (1, 'WAITING'),
        (2, 'SENDING'),
        (3, 'DONE'),
    )
    SEND_TYPE = (
        (1, '全部'),
        (2, '指定服务器'),
        (3, '指定角色'),
    )

    name = models.CharField(max_length=32)
    content = models.TextField()
    send_at = models.DateTimeField(db_index=True)
    send_type = models.IntegerField(choices=SEND_TYPE)
    send_to = models.CharField(max_length=255, blank=True, help_text='指定服务器: id,id  指定角色: id,id')

    attachment = models.ForeignKey(Package, null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STAUTS, default=1, db_index=True)


    def __unicode__(self):
        return self.name

    def clean(self):
        if self.send_type == 2:
            if not self.send_to:
                raise ValidationError("Send to Server Can not be blank")
            for sid in self.send_to.split(','):
                try:
                    sid = int(sid)
                except ValueError:
                    raise ValidationError("id MUST be integer")
                if sid == 0:
                    raise ValidationError("Server id can not be 0")
                if not Server.objects.filter(id=sid).exists():
                    raise ValidationError("Server {0} Does not exists".format(sid))
        elif self.send_type == 3:
            if not self.send_to:
                raise ValidationError("Send to Character Can not be blank")
            for cid in self.send_to.split(','):
                try:
                    cid = int(cid)
                except ValueError:
                    raise ValidationError("id MUST be integer")
                if not Character.objects.filter(id=cid).exists():
                    raise ValidationError("Character {0} Does not exists".format(cid))

    class Meta:
        db_table = 'mail'
        verbose_name = '邮件'
        verbose_name_plural = '邮件'
