from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.purchase.models import Products, PurchaseFailureLog, PurchaseSuccessLog

class ProductsResources(resources.ModelResource):
    class Meta:
        model = Products


class ProductsAdmin(ImportExportModelAdmin):
    list_display = (
        'id', 'name', 'des', 'sycee', 'actual_sycee'
    )

    resource_class = ProductsResources


class PurchaseFailureLogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'char_id', 'buy_date',
        'inner_error', 'apple_error'
    )



class PurchaseSuccessLogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'char_id', 'buy_date', 'product_id', 'actual_sycee',
        'quantity', 'bvrs', 'send_done'
    )


admin.site.register(Products, ProductsAdmin)
admin.site.register(PurchaseFailureLog, PurchaseFailureLogAdmin)
admin.site.register(PurchaseSuccessLog, PurchaseSuccessLogAdmin)
