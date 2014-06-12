from django.contrib import admin

from apps.checkin.models import CheckInDate, CheckInItem, RESOURCE_TYPE

RESOURCE_TYPE_DICT = dict(RESOURCE_TYPE)

class CheckInItemInline(admin.TabularInline):
    model = CheckInItem
    extra = 1
    fieldsets = (
        'index_number',
        'packages',
        ('icon_one_type', 'icon_one_id', 'icon_one_amount'),
        ('icon_two_type', 'icon_two_id', 'icon_two_amount'),
        ('icon_three_type', 'icon_three_id', 'icon_three_amount'),
    )


class CheckIndateAdmin(admin.ModelAdmin):
    list_display = (
        'checkin_date',
    )

    inlines = [CheckInItemInline,]


admin.site.register(CheckInDate, CheckIndateAdmin)
