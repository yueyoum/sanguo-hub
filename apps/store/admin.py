from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.store.models import Store, StoreBuyLog, HEROS, EQUIPMENTS, GEMS, STUFFS

ADMIN_HEROS = dict(HEROS)
ADMIN_EQUIPMENTS = dict(EQUIPMENTS)
ADMIN_GEMS = dict(GEMS)
ADMIN_STUFFS = dict(STUFFS)

ADMIN_ITEM = [0, ADMIN_HEROS, ADMIN_EQUIPMENTS, ADMIN_GEMS, ADMIN_STUFFS]

class StoreResources(resources.ModelResource):
    class Meta:
        model = Store


class StoreAdmin(ImportExportModelAdmin):
    list_display = ('id', 'tag', 'sell_type', 'original_price', 'sell_price',
    'has_total_amount', 'total_amount',
    'has_limit_amount', 'limit_amount',
    'vip_condition', 'level_condition',
    'item_tp', 'Item',
    )

    fieldsets = (
        (None, {
            'fields': ('id', 'tag', 'sell_type', 'original_price', 'sell_price',)
        }),

        ('Item', {
            'fields': ('item_tp', 'hero', 'equipment', 'gem', 'stuff'),
        }),

        ('Condition', {
            'classes': ('collapse', ),
            'fields': ('has_total_amount', 'total_amount',
                        'has_limit_amount', 'limit_amount', 'vip_condition', 'level_condition',
            )
        })
    )

    ordering = ('id',)
    list_filter = ('tag', 'sell_type', 'item_tp',)

    resource_class = StoreResources

    def Item(self, obj):
        return ADMIN_ITEM[obj.item_tp][obj.item_id]


class StoreBuyLogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'sid', 'tag', 'sell_type', 'sell_price',
        'item_tp', 'Item', 'buyer', 'amount', 'buy_at',
    )

    def Item(self, obj):
        return ADMIN_ITEM[obj.item_tp][obj.item_id]



admin.site.register(Store, StoreAdmin)
admin.site.register(StoreBuyLog, StoreBuyLogAdmin)
