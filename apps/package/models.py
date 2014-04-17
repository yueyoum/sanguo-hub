# -*- coding: utf-8 -*-

import json
import os

from django.db import models
from django.conf import settings

FIXTURES_PATH = settings.FIXTURES_PATH

def _make_data(s):
    with open(os.path.join(FIXTURES_PATH, s), 'r') as f:
        data = f.read()

    data = json.loads(data)
    choose = []
    for d in data:
        choose.append((d['pk'], d['fields']['name']))
    choose.sort(key=lambda item: item[0])
    return choose

HEROS = _make_data('heros.json')
EQUIPMENTS = _make_data('equipments.json')
GEMS = _make_data('gems.json')
STUFFS = _make_data('stuffs.json')


class Package(models.Model):
    name = models.CharField(max_length=64, verbose_name='名字')
    gold = models.IntegerField(default=0, verbose_name="金币")
    sycee = models.IntegerField(default=0, verbose_name='元宝')
    exp = models.IntegerField(default=0, verbose_name='经验')
    official_exp = models.IntegerField(default=0, verbose_name='官职经验')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'package'
        verbose_name = "物品包"
        verbose_name_plural = "物品包"


class PackageHero(models.Model):
    package = models.ForeignKey(Package, related_name='package_hero')
    hero = models.IntegerField(choices=HEROS)
    level = models.IntegerField(default=1, verbose_name='强化等级')
    step = models.IntegerField(default=0, verbose_name='进阶阶数')
    amount = models.IntegerField(default=1, verbose_name='数量')
    prob = models.IntegerField(default=100000, verbose_name='概率')

    class Meta:
        db_table = 'package_hero'


class PackageHeroSoul(models.Model):
    package = models.ForeignKey(Package, related_name='package_hero_soul')
    soul = models.IntegerField(choices=HEROS)
    amount = models.IntegerField(default=1, verbose_name='数量')
    prob = models.IntegerField(default=100000, verbose_name='概率')

    class Meta:
        db_table = 'package_hero_soul'


class PackageEquipment(models.Model):
    package = models.ForeignKey(Package, related_name='package_equipment')
    equipment = models.IntegerField(choices=EQUIPMENTS)
    level = models.IntegerField(default=1, verbose_name='强化等级')
    amount = models.IntegerField(default=1, verbose_name='数量')
    prob = models.IntegerField(default=100000, verbose_name='概率')

    class Meta:
        db_table = 'package_equip'


class PackageGem(models.Model):
    package = models.ForeignKey(Package, related_name='package_gem')
    gem = models.IntegerField(choices=GEMS)
    amount = models.IntegerField(default=1, verbose_name='数量')
    prob = models.IntegerField(default=100000, verbose_name='概率')

    class Meta:
        db_table = 'package_gem'


class PackageStuff(models.Model):
    package = models.ForeignKey(Package, related_name='package_stuff')
    stuff = models.IntegerField(choices=STUFFS)
    amount = models.IntegerField(default=1, verbose_name='数量')
    prob = models.IntegerField(default=100000, verbose_name='概率')

    class Meta:
        db_table = 'package_stuff'

