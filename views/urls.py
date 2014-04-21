# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'

from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^world/server-list/$', 'views.dispatch.server.views.server_list'),
                       url(r'^player/register/$', 'views.dispatch.account.views.register'),

                       url(r'^api/server-list/$', 'views.api.server.views.server_list'),
                       url(r'^api/server-list/report/$', 'views.api.server.views.server_list_report'),
                       url(r'^api/account/login/$', 'views.api.account.views.login'),
                       url(r'^api/character/create/$', 'views.api.character.views.create'),
                       # url(r'^api/character/find/$', 'views.api.character.views.find_char_id'),

                       url(r'^api/purchase/products/$', 'views.api.purchase.views.get_products'),
                       url(r'^api/purchase/save-log/$', 'views.api.purchase.views.save_log'),
                       url(r'^api/purchase/send-done/$', 'views.api.purchase.views.send_done'),
)
