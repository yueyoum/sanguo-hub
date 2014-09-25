# -*- coding: utf-8 -*-


from django.db import models

from core.fixtures import HEROS, EQUIPMENTS, GEMS, STUFFS


class Package(models.Model):
    MODE = (
        (1, '默认'),
        (2, '只生成一样'),
    )
    name = models.CharField(max_length=64, verbose_name='名字')
    mode = models.IntegerField(choices=MODE, default=1)
    gold = models.IntegerField(default=0, verbose_name="金币")
    sycee = models.IntegerField(default=0, verbose_name='元宝')
    exp = models.IntegerField(default=0, verbose_name='经验')
    official_exp = models.IntegerField(default=0, verbose_name='官职经验')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'package'
        ordering = ('-id',)
        verbose_name = "物品包"
        verbose_name_plural = "物品包"


    def export_data(self):
        data = {
            'mode': self.mode,
            'gold': self.gold,
            'sycee': self.sycee,
            'exp': self.exp,
            'official_exp': self.official_exp,
        }

        heros = self.package_hero.all()
        heros_data = []
        for h in heros:
            heros_data.append({
                'id': h.hero,
                'amount': h.amount,
                'prob': h.prob,
            })

        souls = self.package_soul.all()
        souls_data = []
        for s in souls:
            souls_data.append({
                'id': s.soul,
                'amount': s.amount,
                'prob': s.prob,
            })

        equips = self.package_equipment.all()
        equips_data = []
        for e in equips:
            equips_data.append({
                'id': e.equipment,
                'level': e.level,
                'amount': e.amount,
                'prob': e.prob,
            })

        gems = self.package_gem.all()
        gems_data = []
        for g in gems:
            gems_data.append({
                'id': g.gem,
                'amount': g.amount,
                'prob': g.prob,
            })

        stuffs = self.package_stuff.all()
        stuffs_data = []
        for s in stuffs:
            stuffs_data.append({
                'id': s.stuff,
                'amount': s.amount,
                'prob': s.prob,
            })

        data['heros'] = heros_data
        data['souls'] = souls_data
        data['equipments'] = equips_data
        data['gems'] = gems_data
        data['stuffs'] = stuffs_data
        return data



class PackageHero(models.Model):
    package = models.ForeignKey(Package, related_name='package_hero')
    hero = models.IntegerField(choices=HEROS)
    amount = models.IntegerField(default=1, verbose_name='数量')
    prob = models.IntegerField(default=100000, verbose_name='概率')

    class Meta:
        db_table = 'package_hero'


class PackageSoul(models.Model):
    package = models.ForeignKey(Package, related_name='package_soul')
    soul = models.IntegerField(choices=HEROS)
    amount = models.IntegerField(default=1, verbose_name='数量')
    prob = models.IntegerField(default=100000, verbose_name='概率')

    class Meta:
        db_table = 'package_soul'


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

