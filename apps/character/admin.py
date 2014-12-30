# -*- coding:utf-8 -*-

import json

from django.http import HttpResponse
from django.contrib import admin
from django import forms
from django.contrib.admin.helpers import ActionForm
from django.contrib import messages

from apps.character.models import Character
from utils.api import api_character_information, api_character_union


class MyActionForm(ActionForm):
    value = forms.CharField()


class CharacterAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'account_id', 'server_id', 'name')

    list_display = ('id', 'account_id', 'server_id', 'name', 'create_at',
    )
    search_fields = ['name',]
    list_per_page = 100

    action_form = MyActionForm
    actions = ['show_basic_information', 'query_joined_union', 'add_sycee',]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    # custom actions
    def show_basic_information(self, request, queryset):
        # selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        result = []
        for q in queryset:
            data = api_character_information(q.server_id, q.id)['data']
            result.append({
                '角色ID': q.id,
                '角色名字': q.name,
                '银币': data['gold'],
                '元宝': data['sycee'],
                '等级': data['level'],
                '经验': data['exp'],
                'VIP': data['vip'],
            })

        return HttpResponse(json.dumps(result), content_type='application/json')
    show_basic_information.short_description = "角色基本信息"


    def query_joined_union(self, request, queryset):
        result = []
        for q in queryset:
            data = api_character_union(q.server_id, q.id)['data']
            result.append({
                '角色ID': q.id,
                '角色名字': q.name,
                '工会ID': data['union'],
                '会长ID': data['union_owner'],
                '工会名字': data['union_name'],
                '工会公告': data['union_bulletin'],
                '工会等级': data['union_level'],
                '工会贡献度': data['union_contribute_points'],
                '工会积分': data['union_score'],
                '成员工会币': data['member_coin'],
                '成员贡献度': data['member_contribute_points'],
                '成员职位': data['member_position'],
                '成员签到次数': data['member_checkin_times'],
                '成员打BOSS次数': data['member_boss_times'],
                '成员买BUFF次数': data['member_buy_buff_times'],
            })

        response = HttpResponse(json.dumps(result), content_type='application/json')
        return response

    query_joined_union.short_description = "查看加入的工会"


    def add_sycee(self, request, queryset):
        if queryset.count() > 1:
            self.message_user(request, "只能选择一个角色修改", level=messages.ERROR)
            return

        try:
            value = int(request.POST['value'])
            assert value > 0
        except:
            self.message_user(request, "填入的数字错误", level=messages.ERROR)
            return

        print queryset[0].id, value




admin.site.register(Character, CharacterAdmin)
