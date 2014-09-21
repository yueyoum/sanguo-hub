# -*- coding: utf-8 -*-

import os
import time
import hashlib

from django.db import models


def _bulletin_upload_to(instance, filename):
    name, ext = os.path.splitext(filename)
    sign = '{0}{1}'.format(name, time.time())
    new_name = '%s%s' % (hashlib.md5(sign).hexdigest(), ext)
    return os.path.join('bulletin', new_name)


class BulletinConfig(models.Model):
    window_width = models.IntegerField("窗口宽度", default=400)
    window_margin = models.IntegerField("窗口边距", default=10)
    window_bg_color = models.CharField("窗口背景颜色", default="ffffff", max_length=6)
    window_bg_image = models.FileField("窗口背景图片", blank=True, upload_to=_bulletin_upload_to)

    bulletin_window_border_radius = models.IntegerField("公告窗体边角半径", default=10)

    bulletin_title_size = models.FloatField("公告标题字体大小", default=1.5)
    bulletin_title_color = models.CharField("默认公告标题颜色", default="000000", max_length=6)
    bulletin_title_bg_color = models.CharField("默认公告标题背景颜色", default="ffffff", max_length=6)
    bulletin_title_bg_image = models.FileField("默认公告标题背景图片", blank=True, upload_to=_bulletin_upload_to)

    bulletin_content_size = models.FloatField("公告内容字体大小", default=1)
    bulletin_content_color = models.CharField("默认公告内容颜色", default="000000", max_length=6)
    bulletin_content_bg_color = models.CharField("默认公告内容背景颜色", default="ffffff", max_length=6)
    bulletin_content_bg_image = models.FileField("默认公告内容背景图片", blank=True, upload_to=_bulletin_upload_to)


    class Meta:
        db_table = 'bulletin_config'
        verbose_name = "系统公告基本配置"
        verbose_name_plural = "系统公告基本配置"


class Bulletin(models.Model):
    title = models.CharField("标题", max_length=64)
    content = models.TextField("内容", blank=True)
    content_image = models.FileField("内容图片", blank=True, upload_to=_bulletin_upload_to)

    order_seq = models.IntegerField("排列序号", default=0, help_text="数值越大排列位置越靠前")
    create_time = models.DateTimeField(auto_now_add=True)

    title_color = models.CharField("标题颜色", blank=True, max_length=6)
    title_bg_color = models.CharField("标题背景颜色", blank=True, max_length=6)
    title_bg_image = models.FileField("标题背景图片", blank=True,  upload_to=_bulletin_upload_to)

    content_color = models.CharField("内容颜色", blank=True, max_length=6)
    content_bg_color = models.CharField("背景颜色", blank=True, max_length=6)
    content_bg_image = models.FileField("背景图片", blank=True, upload_to=_bulletin_upload_to)

    display = models.BooleanField("是否显示", default=False, db_index=True)


    class Meta:
        db_table = 'bulletin'
        index_together = (('order_seq', 'create_time'),)
        verbose_name = "系统公告"
        verbose_name_plural = "系统公告"


