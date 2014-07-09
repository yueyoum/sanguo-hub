from django.db import models

from apps.store.models import AbstractStore

class StoreProduction(AbstractStore):
    class Meta:
        db_table = 'store_production'
