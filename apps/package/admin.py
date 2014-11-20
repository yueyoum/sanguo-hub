# -*- coding: utf-8 -*-

from django.contrib import admin

from apps.package.models import (
    Package,
    PackageHero,
    PackageSoul,
    PackageEquipment,
    PackageGem,
    PackageStuff,

    HEROS,
    EQUIPMENTS,
    GEMS,
    STUFFS,
)

HEROS_DICT = dict(HEROS)
EQUIPMENTS_DICT = dict(EQUIPMENTS)
GEMS_DICT = dict(GEMS)
STUFFS_DICT = dict(STUFFS)

class HeroInfoInline(admin.TabularInline):
    model = PackageHero
    extra = 1

class SoulInfoInline(admin.TabularInline):
    model = PackageSoul
    extra = 1

class EquipInfoInline(admin.TabularInline):
    model = PackageEquipment
    extra = 1

class GemInfoInline(admin.TabularInline):
    model = PackageGem
    extra = 1

class StuffInfoInline(admin.TabularInline):
    model = PackageStuff
    extra = 1

class PackageAdmin(admin.ModelAdmin):
    inlines = (
        HeroInfoInline, SoulInfoInline, EquipInfoInline,
        GemInfoInline, StuffInfoInline
    )

    list_display = ('id', 'name', 'mode', 'gold', 'sycee', 'exp', 'official_exp', 'Heros', 'Souls', 'Equips', 'Gems', 'Stuffs')


    def Heros(self, obj):
        data = obj.package_hero.all()
        def _make_text(x):
            text = u'{0}, 数量: {1}, 概率: {2}'.format(
                HEROS_DICT[x.hero], x.amount, x.prob
            )
            return text
        texts = [_make_text(x) for x in data]
        return '<br />'.join(texts)
    Heros.allow_tags = True


    def Souls(self, obj):
        data = obj.package_soul.all()
        def _make_text(x):
            text = u'{0}, 数量: {1}, 概率: {2}'.format(
                HEROS_DICT[x.soul], x.amount, x.prob
            )
            return text
        texts = [_make_text(x) for x in data]
        return '<br />'.join(texts)
    Souls.allow_tags = True


    def Equips(self, obj):
        data = obj.package_equipment.all()
        def _make_text(x):
            text = u'{0}, 等级: {1},  数量: {2}, 概率: {3}'.format(
                EQUIPMENTS_DICT[x.equipment], x.level, x.amount, x.prob
            )
            return text
        texts = [_make_text(x) for x in data]
        return '<br />'.join(texts)
    Equips.allow_tags = True

    def Gems(self, obj):
        data = obj.package_gem.all()
        def _make_text(x):
            text = u'{0}, 数量: {1}, 概率: {2}'.format(
                GEMS_DICT[x.gem], x.amount, x.prob
            )
            return text
        texts = [_make_text(x) for x in data]
        return '<br />'.join(texts)
    Gems.allow_tags = True


    def Stuffs(self, obj):
        data = obj.package_stuff.all()
        def _make_text(x):
            text = u'{0}, 数量: {1}, 概率: {2}'.format(
                STUFFS_DICT[x.stuff], x.amount, x.prob
            )
            return text
        texts = [_make_text(x) for x in data]
        return '<br />'.join(texts)
    Stuffs.allow_tags = True


admin.site.register(Package, PackageAdmin)
