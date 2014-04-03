from django.contrib import admin

from apps.server.models import ServerNode, Server

STATUS_DICT = dict(Server.STATUS)

class ServerInLine(admin.TabularInline):
    model = Server

class ServerNodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'port', 'Servers')

    inlines = [ServerInLine,]

    def Servers(self, obj):
        servers = obj.servers.all()
        def _make_text(s):
            return '{0}  {1}  {2}'.format(s.id, s.name.encode('utf-8'), STATUS_DICT[s.status])

        texts = [_make_text(s) for s in servers]
        return '<br />'.join(texts)
    Servers.allow_tags = True


admin.site.register(ServerNode, ServerNodeAdmin)

