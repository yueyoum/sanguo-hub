from django.contrib import admin

from apps.broadcast.models import Broadcast

class BroadcastAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'create_at', 'display')

    exclude = ('image', 'link')


admin.site.register(Broadcast, BroadcastAdmin)
