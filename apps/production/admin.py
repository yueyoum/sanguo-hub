from django.contrib import admin

from apps.production.models import StoreProduction
from apps.store.admin import ADMIN_ITEM

# This is copy from StoreAdmin
class StoreProductionAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'sell_type', 'original_price', 'sell_price',
    'has_total_amount', 'total_amount', 'total_amount_run_time',
    'has_limit_amount', 'limit_amount',
    'vip_condition', 'level_condition',
    'item_tp', 'Item',
    )

    ordering = ('id',)
    list_filter = ('tag', 'sell_type', 'item_tp',)


    def Item(self, obj):
        return ADMIN_ITEM[obj.item_tp][obj.item_id]

    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(StoreProduction, StoreProductionAdmin)
