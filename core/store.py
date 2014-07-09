# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/22/14'

from django.db import transaction

from apps.production.models import StoreProduction
from apps.store.models import StoreBuyLog
from preset import errormsg


def newest_store_goods():
    store = {}
    fields = [f.name for f in StoreProduction._meta.fields]
    for s in StoreProduction.objects.all():
        data = {}
        for f in fields:
            data[f] = getattr(s, f)
            data['item_id'] = s.item_id

        store[s.id] = data

    return store


class Store(object):
    def buy(self, data):
        try:
            char_id = int(data['char_id'])
            goods_id = int(data['goods_id'])
            goods_amount = int(data['goods_amount'])
        except (KeyError, ValueError):
            return {'ret': errormsg.BAD_MESSAGE}

        store = newest_store_goods()

        if goods_id not in store:
            return {'ret': errormsg.STORE_GOODS_NOT_EXIST}

        data = {}

        if store[goods_id]['has_total_amount']:
            with transaction.atomic():
                try:
                    g = StoreProduction.objects.select_for_update().get(id=goods_id)
                except StoreProduction.DoesNotExist:
                    return {'ret': errormsg.STORE_GOODS_NOT_EXIST}

                if g.total_amount_run_time < goods_amount:
                    return {'ret': errormsg.STORE_GOODS_AMOUNT_NOT_ENOUGH}

                g.total_amount_run_time -= goods_amount
                g.save()
                data['total_amount_run_time'] = g.total_amount_run_time

        self.save_log(char_id, goods_id, goods_amount, store)
        return {'ret': 0, 'data': data}


    def save_log(self, char_id, goods_id, goods_amount, store):
        goods = store[goods_id]
        StoreBuyLog.objects.create(
            sid=goods_id,
            tag=goods['tag'],
            sell_type=goods['sell_type'],
            sell_price=goods['sell_price'],
            item_tp=goods['item_tp'],
            item_id=goods['item_id'],
            buyer=char_id,
            amount=goods_amount,
        )
