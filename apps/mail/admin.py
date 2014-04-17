from django.contrib import admin

from apps.mail.models import Mail

class MailAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content', 'send_at', 'attachment', 'create_at', 'status')

    exclude = ('create_at', 'status',)


admin.site.register(Mail, MailAdmin)
