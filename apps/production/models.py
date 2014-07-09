# -*- coding: utf-8 -*-

from django.db import models

from apps.store.models import AbstractStore

class StoreProduction(AbstractStore):
    class Meta:
        db_table = 'store_production'
        verbose_name = "商场-正式"
        verbose_name_plural = "商场-正式"

