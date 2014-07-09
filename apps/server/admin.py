from django.contrib import admin

from apps.server.models import Server
from apps.character.models import Character


class ServerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'host', 'port', 'port_https', 'Players', 'active_players')

    def Players(self, obj):
        return Character.objects.filter(server_id=obj.id).count()

admin.site.register(Server, ServerAdmin)
