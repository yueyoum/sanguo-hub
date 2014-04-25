# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/22/14'

from django.db import transaction

from apps.store.models import Store as ModelStore, StoreBuyLog

STORE = None

def _get_store_goods():
    global STORE
    if STORE:
        return

    STORE = {}
    fields = ModelStore._meta.get_all_field_names()

    for s in ModelStore.objects.all():
        data = {}
        for f in fields:
            data[f] = getattr(s, f)
            data['item_id'] = s.item_id
        STORE[s.id] = data

_get_store_goods()


def newest_store_goods():
    goods = ModelStore.objects.filter(has_total_amount=True).only('total_amount_run_time').all()
    for g in goods:
        STORE[g.id]['total_amount_run_time'] = g.total_amount_run_time
    return STORE



class Store(object):
    def buy(self, data):
        try:
            char_id = int(data['char_id'])
            goods_id = int(data['goods_id'])
            goods_amount = int(data['goods_amount'])
        except (KeyError, ValueError):
            return {'ret': 1}

        if goods_id not in STORE:
            return {'ret': 60}

        data = {}

        if STORE[goods_id]['has_total_amount']:
            with transaction.atomic():
                try:
                    g = ModelStore.objects.select_for_update().get(id=goods_id)
                except ModelStore.DoesNotExist:
                    return {'ret': 60}

                if g.total_amount_run_time < goods_amount:
                    return {'ret': 61}

                g.total_amount_run_time -= goods_amount
                g.save()
                data['total_amount_run_time'] = g.total_amount_run_time

        self.save_log(char_id, goods_id, goods_amount)
        return {'ret': 0, 'data': data}


    def save_log(self, char_id, goods_id, goods_amount):
        goods = STORE[goods_id]
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
