from django.contrib import admin

from apps.purchase.models import Products, PurchaseFailureLog, PurchaseSuccessLog


class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'des', 'sycee', 'actual_sycee'
    )


class PurchaseFailureLogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'product_id', 'actual_sycee', 'char_id', 'buy_date', 'receipt',
        'inner_error', 'apple_error'
    )



class PurchaseSuccessLogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'product_id', 'actual_sycee', 'char_id', 'buy_date', 'receipt',
        'quantity', 'bvrs', 'send_done'
    )


admin.site.register(Products, ProductsAdmin)
admin.site.register(PurchaseFailureLog, PurchaseFailureLogAdmin)
admin.site.register(PurchaseSuccessLog, PurchaseSuccessLogAdmin)
