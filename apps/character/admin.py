# -*- coding:utf-8 -*-

from django.contrib import admin

from apps.character.models import Character
from utils.api import api_character_information

class CharacterAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'account_id', 'server_id', 'name')

    list_display = ('id', 'account_id', 'server_id', 'name', 'create_at',
    'Sycee', 'Gold', 'Level', 'Exp', 'Vip'
    )
    search_fields = ['name',]
    list_per_page = 50

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def _get_char_info(self, obj):
        all_info = getattr(self, '__char_info', {})
        info = all_info.get(obj.id, None)
        if not info:
            info = api_character_information(obj.server_id, obj.id)
            all_info[obj.id] = info
            setattr(self, '__char_info', all_info)
        return info

    def Gold(self, obj):
        return self._get_char_info(obj)['gold']
    Gold.short_description = "银两"

    def Sycee(self, obj):
        return self._get_char_info(obj)['sycee']
    Sycee.short_description = "元宝"

    def Level(self, obj):
        return self._get_char_info(obj)['level']
    Level.short_description = "等级"

    def Exp(self, obj):
        return self._get_char_info(obj)['exp']
    Exp.short_description = "经验"

    def Vip(self, obj):
        return self._get_char_info(obj)['vip']


admin.site.register(Character, CharacterAdmin)
