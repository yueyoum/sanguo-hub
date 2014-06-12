from django.contrib import admin

from apps.checkin.models import CheckInDate, CheckInItem, RESOURCE_TYPE

RESOURCE_TYPE_DICT = dict(RESOURCE_TYPE)

class CheckInItemInline(admin.TabularInline):
    model = CheckInItem
    extra = 1


class CheckIndateAdmin(admin.ModelAdmin):
    list_display = (
        'checkin_date',
    )

    inlines = [CheckInItemInline,]


admin.site.register(CheckInDate, CheckIndateAdmin)
