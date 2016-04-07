from django.contrib import admin


from apps.purchase.models import (
    PurchaseSelfLog,
    PurchaseIOSSuccessLog,
    PurchaseIOSErrorLog,
    Purchase91Log,
    PurchaseAiyingyongLog,
    PurchaseAllSdkLog,
    PurchaseJodoPlayLog,
)

class PurchaseSelfLogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'server_id', 'char_id', 'goods_id', 'rmb', 'amount', 'buy_time'
    )

    exclude = ('server_id', 'rmb',)

    def has_delete_permission(self, request, obj=None):
        return False


class PurchaseIOSSuccessLogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'transaction_id', 'server_id', 'char_id',
        'product_id', 'quantity', 'order_money', 'buy_time'
    )


    def has_delete_permission(self, request, obj=None):
        return False


class PurchaseIOSErrorLogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'server_id', 'char_id', 'error_code', 'buy_time',
    )


    def has_delete_permission(self, request, obj=None):
        return False


class Purchase91LogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'order_id', 'order_time', 'server_id', 'char_id', 'goods_id', 'is_test_mode',
        'consume_stream_id', 'uid',
        'original_money', 'order_money', 'note',
        'pay_status', 'create_time',
    )

    def has_delete_permission(self, request, obj=None):
        return False


class PurchaseAiyingyongLogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'order_id', 'order_time', 'server_id', 'char_id', 'goods_id', 'order_money', 'confirmed'
    )


    def has_delete_permission(self, request, obj=None):
        return False


class PurchaseAllSDKLogAdmin(admin.ModelAdmin):
    list_display = (
        'sn', 'return_code', 'order_time', 'server_id', 'char_id', 'goods_id', 'order_money', 'verify_time', 'verify_ok'
    )


    def has_delete_permission(self, request, obj=None):
        return False


class PurchaseJodoPlayLogAdmin(admin.ModelAdmin):
    list_display = (
        'order_id', 'order_time', 'server_id', 'char_id', 'goods_id',
        'jodo_order_id', 'jodo_price', 'uid', 'pay_at', 'confirmed'
    )

    search_fields = ('char_id',)

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(PurchaseSelfLog, PurchaseSelfLogAdmin)
admin.site.register(PurchaseIOSSuccessLog, PurchaseIOSSuccessLogAdmin)
admin.site.register(PurchaseIOSErrorLog, PurchaseIOSErrorLogAdmin)
admin.site.register(Purchase91Log, Purchase91LogAdmin)
admin.site.register(PurchaseAiyingyongLog, PurchaseAiyingyongLogAdmin)
admin.site.register(PurchaseAllSdkLog, PurchaseAllSDKLogAdmin)
admin.site.register(PurchaseJodoPlayLog, PurchaseJodoPlayLogAdmin)
