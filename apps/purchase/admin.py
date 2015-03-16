from django.contrib import admin


from apps.purchase.models import PurchaseIOSSuccessLog, PurchaseIOSErrorLog, Purchase91Log, PurchaseAiyingyongLog, PurchaseAllSdkLog


class PurchaseIOSSuccessLogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'transaction_id', 'server_id', 'char_id',
        'product_id', 'quantity', 'order_money', 'buy_time'
    )



class PurchaseIOSErrorLogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'server_id', 'char_id', 'error_code', 'buy_time',
    )


class Purchase91LogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'order_id', 'order_time', 'server_id', 'char_id', 'goods_id', 'is_test_mode',
        'consume_stream_id', 'uid',
        'original_money', 'order_money', 'note',
        'pay_status', 'create_time',
    )


class PurchaseAiyingyongLogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'order_id', 'order_time', 'server_id', 'char_id', 'goods_id', 'order_money', 'confirmed'
    )

class PurchaseAllSDKLogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'sn', 'return_code', 'order_time', 'server_id', 'char_id', 'goods_id', 'order_money', 'verify_ok'
    )

admin.site.register(PurchaseIOSSuccessLog, PurchaseIOSSuccessLogAdmin)
admin.site.register(PurchaseIOSErrorLog, PurchaseIOSErrorLogAdmin)
admin.site.register(Purchase91Log, Purchase91LogAdmin)
admin.site.register(PurchaseAiyingyongLog, PurchaseAiyingyongLogAdmin)
admin.site.register(PurchaseAllSdkLog, PurchaseAllSDKLogAdmin)
