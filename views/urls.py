# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/1/14'

from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       # called from client directly
                       url(r'^world/server-list/$', 'views.server.views.server_list'),
                       url(r'^player/register/$', 'views.account.views.register'),
                       url(r'^system/bulletin/$', 'views.system.views.get_bulletins'),

                       url(r'^callback/91/$', 'views.callback.views.purchase_91_notify'),
                       url(r'^callback/test91/$', 'views.callback.views.purchase_91_notify'),

                       url(r'^callback/aiyingyong/$', 'views.callback.views.purchase_aiyingyong_notify'),
                       url(r'^callback/jodoplay/$', 'views.callback.views.purchase_jodoplay_notify'),

                        # API called from server
                       url(r'^api/server-list/$', 'views.api.server.views.server_list'),
                       url(r'^api/server-list/register/$', 'views.api.server.views.server_register_view'),

                       url(r'^api/account/login/$', 'views.api.account.views.login'),
                       url(r'^api/account/bind/$', 'views.api.account.views.bind'),
                       url(r'^api/character/create/$', 'views.api.character.views.create'),
                       url(r'^api/store/get/$', 'views.api.store.views.get'),
                       url(r'^api/store/buy/$', 'views.api.store.views.buy'),

                       url(r'^api/activatecode/use/$', 'views.api.activatecode.views.use'),
                       url(r'^api/checkin/get/$', 'views.api.checkin.views.get_checkin_package'),

                       url(r'^api/purchase/verify/$', 'views.api.purchase.views.ios_verify'),
                       url(r'^api/purchase/allsdk/verify/$', 'views.api.purchase.views.allsdk_verify'),

                       url(r'^api/purchase/orderid/$', 'views.api.purchase.views.get_purchase_order_id'),
                       url(r'^api/purchase/91/confirm/$', 'views.api.purchase.views.purchase91_confirm'),
                       url(r'^api/purchase/aiyingyong/confirm/$', 'views.api.purchase.views.purchase_aiyingyong_confirm'),
                       url(r'^api/purchase/jodoplay/confirm/$', 'views.api.purchase.views.purchase_jodoplay_confirm'),

                       url(r'^api/system/broadcast/$', 'views.api.system.views.get_system_broadcast'),
)
