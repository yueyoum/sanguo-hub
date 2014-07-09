# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-7-9'

import json

from django.core.management.base import BaseCommand
from django.db import transaction


def make_new_objs(old_model, new_model):
    fields = [f.name for f in old_model._meta.fields]

    def _make(obj):
        new_obj = new_model()
        for f in fields:
            value = getattr(obj, f)
            setattr(new_obj, f, value)
        return new_obj

    return [_make(obj) for obj in old_model.objects.all()]



class Command(BaseCommand):
    help = """Load Config. args:
    store       reload store config.
    checkin     notify servers
    """

    def handle(self, *args, **options):
        if not args:
            self.stdout.write(self.help)
            return

        if args[0] == 'store':
            self._cmd_load_store()
        elif args[0] == 'checkin':
            self._cmd_load_checkin()
        else:
            self.stdout.write(self.help)
            return

    @transaction.atomic
    def _cmd_load_store(self):
        from apps.production.models import StoreProduction
        from apps.store.models import Store

        StoreProduction.objects.all().delete()

        new_objs = make_new_objs(Store, StoreProduction)
        StoreProduction.objects.bulk_create(new_objs)


    @transaction.atomic
    def _cmd_load_checkin(self):
        from core.checkin import get_checkin_obj
        from utils.api import api_send_checkin_data

        data = get_checkin_obj().export_data()
        api_send_checkin_data(data=json.dumps(data))
