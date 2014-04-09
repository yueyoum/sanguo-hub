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
)
