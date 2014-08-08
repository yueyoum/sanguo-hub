# -*- coding: utf-8 -*-
import os
import hashlib
import string


from django.db import models
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError


class ActivateBucket(models.Model):
    name = models.CharField("名称", max_length=32)
    des = models.TextField("描述", blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    code_amount = models.PositiveIntegerField("数量", default=100)
    code_length = models.PositiveIntegerField("长度", default=16, help_text='min: 12, max: 40')

    can_use = models.BooleanField("可以使用", default=True)
    use_times_limit = models.PositiveIntegerField("可以用的次数", default=0, help_text='0 表示没有限制')

    has_date_limit = models.BooleanField("是否有使用时间限制", default=False)
    active_start = models.DateField("可用起始时间", null=True, blank=True)
    active_end = models.DateField("可用结束时间", null=True, blank=True)

    package = models.ForeignKey('package.Package')

    class Meta:
        db_table = 'activate_bucket'
        verbose_name = '激活码生成'
        verbose_name_plural = '激活码生成'

    def clean(self):
        if self.code_length < 12 or self.code_length > 40:
            raise ValidationError("Invalid code length")

        if self.has_date_limit:
            if not self.active_start or not self.active_end:
                raise ValidationError("Must set date")

            if self.active_end <= self.active_start:
                raise ValidationError("date end should greater than date start")

        if self.active_start:
            if not self.has_date_limit or not self.active_end:
                raise ValidationError("check date limit setting")

        if self.active_end:
            if not self.has_date_limit or not self.active_start:
                raise ValidationError("check date limit setting")


class ActivateCode(models.Model):
    code_id = models.CharField(unique=True, max_length=40)
    bucket = models.ForeignKey(ActivateBucket, related_name='codes')

    class Meta:
        db_table = 'activate_code'


class ActivateCodeUseLog(models.Model):
    code_id = models.CharField(db_index=True, max_length=40)
    # who use
    char_id = models.IntegerField("角色ID")
    used_at = models.DateTimeField("使用时间", auto_now_add=True)

    class Meta:
        db_table = 'activate_code_log'

        unique_together = (('code_id', 'char_id'),)
        verbose_name = '激活码使用记录'
        verbose_name_plural = '激活码使用记录'

_table = string.maketrans('0123456789', 'abcdefghij')
def generate_codes(amount, length=16):
    for i in range(amount):
        codes = hashlib.md5(os.urandom(32)).hexdigest()
        codes = codes[:length]
        yield codes.translate(_table)

def _generate_and_save_codes(sender, instance, created, **kwargs):
    if not created:
        return

    objs = []
    for c in generate_codes(instance.code_amount, length=instance.code_length):
        objs.append(ActivateCode(code_id=c, bucket=instance))

    ActivateCode.objects.bulk_create(objs)

post_save.connect(
    _generate_and_save_codes,
    sender=ActivateBucket,
    dispatch_uid='_generate_and_save_codes'
)

