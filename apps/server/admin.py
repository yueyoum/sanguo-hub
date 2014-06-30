from django.contrib import admin

from apps.server.models import Server


class ServerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'host', 'port', 'port_https', 'players', 'active_players')

admin.site.register(Server, ServerAdmin)
