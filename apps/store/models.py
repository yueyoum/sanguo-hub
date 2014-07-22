# -*- coding: utf-8 -*-

from django.db import models

from core.fixtures import HEROS, EQUIPMENTS, GEMS, STUFFS

STORE_TAG = (
    (1, '促销'),
    (2, '商城'),
    (3, 'VIP专卖'),
)

SELL_TYPE = (
    (1, '金币'),
    (2, '元宝'),
)

ITEM_TP = (
    (1, '武将'),
    (2, '装备'),
    (3, '宝石'),
    (4, '道具'),
)


class AbstractStore(models.Model):
    id = models.IntegerField(primary_key=True)
    tag = models.IntegerField("标签", choices=STORE_TAG)
    sell_type = models.IntegerField("售卖类型", choices=SELL_TYPE)
    original_price = models.IntegerField("原价")
    sell_price = models.IntegerField("售价")

    has_total_amount = models.BooleanField("是否总量限制", default=False, db_index=True)
    total_amount = models.IntegerField("总量", default=0, help_text='如果没有总量限制，则此数值无意义')

    has_limit_amount = models.BooleanField("是否每人每天限购", default=False)
    limit_amount = models.IntegerField("每人每天限购数量", default=0, help_text='如果没有限购，则此数无意义')

    vip_condition = models.IntegerField("VIP等级需求", default=0, help_text='VIP多少级才可以购买')
    level_condition = models.IntegerField("君主等级需求", default=0, help_text='君主等级多上级才可以购买')

    item_tp = models.IntegerField("物品类型", choices=ITEM_TP)
    hero = models.IntegerField('武将', choices=HEROS, null=True, blank=True)
    equipment = models.IntegerField('装备', choices=EQUIPMENTS, null=True, blank=True)
    gem = models.IntegerField('宝石', choices=GEMS, null=True, blank=True)
    stuff = models.IntegerField('道具', choices=STUFFS, null=True, blank=True)

    active = models.BooleanField('售卖中', default=True, db_index=True)

    class Meta:
        abstract = True

    @property
    def item_id(self):
        if self.item_tp == 1:
            return self.hero
        if self.item_tp == 2:
            return self.equipment
        if self.item_tp == 3:
            return self.gem

        return self.stuff


class Store(AbstractStore):
    class Meta:
        db_table = 'store'
        ordering = ('id',)
        verbose_name = '商城'
        verbose_name_plural = '商城'



class StoreBuyLog(models.Model):
    sid = models.IntegerField("商品ID")
    tag = models.IntegerField("商城", choices=STORE_TAG)
    sell_type = models.IntegerField("售卖类型", choices=SELL_TYPE)
    sell_price = models.IntegerField("售价")

    item_tp = models.IntegerField("物品类型", choices=ITEM_TP)
    item_id = models.IntegerField("物品ID")

    buyer = models.IntegerField("购买者ID")
    amount = models.IntegerField("购买数量")
    buy_at = models.DateTimeField("购买日期", auto_now_add=True)

    class Meta:
        db_table = 'store_log'
        verbose_name = '购买记录'
        verbose_name_plural = '购买记录'
