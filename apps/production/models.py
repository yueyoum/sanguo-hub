# -*- coding: utf-8 -*-

import random

from django.db import models

from apps.store.models import AbstractStore

class StoreProduction(AbstractStore):
    total_amount_run_time = models.IntegerField("实时总量", default=0)

    class Meta:
        db_table = 'store_production'
        verbose_name = "商场-正式"
        verbose_name_plural = "商场-正式"

    @classmethod
    def make_random_tag_one(cls, amount=6):
        # 促销商品每天变化
        # 这个方法会将amount个促销商品的active设置为True
        # 其他为False，这样其他促销商品就买不到了
        this_tag_goods = cls.objects.filter(tag=1).values_list('id', flat=True)
        this_tag_goods = list(this_tag_goods)

        cls.objects.filter(id__in=this_tag_goods).update(active=False)

        choosing = []
        while True:
            if not this_tag_goods:
                break
            if len(choosing) >= amount:
                break

            _id = random.choice(this_tag_goods)
            this_tag_goods.remove(_id)
            if _id not in choosing:
                choosing.append(_id)

        cls.objects.filter(id__in=choosing).update(active=True)
