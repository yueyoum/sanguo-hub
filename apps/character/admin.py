from django.contrib import admin

from apps.character.models import Character

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'account_id', 'server_id', 'name', 'create_at')
    search_fields = ['name',]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Character, CharacterAdmin)
