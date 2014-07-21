# -*- coding: utf-8 -*-

from django.db import models


class Broadcast(models.Model):
    title = models.CharField("标题", max_length=64)
    image = models.CharField("图片", max_length=255, blank=True)
    content = models.TextField("内容")
    link = models.IntegerField("页面链接", blank=True, null=True)

    create_at = models.DateTimeField(auto_now_add=True)
    display = models.BooleanField("是否显示", default=True, db_index=True)

    class Meta:
        db_table = 'broadcast'
        verbose_name = '系统广播'
        verbose_name_plural = '系统广播'
