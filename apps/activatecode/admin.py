
import base64
from django.contrib import admin

from apps.activatecode.models import ActivateBucket, ActivateCode, ActivateCodeUseLog

class ActivateBucketAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'des', 'create_at', 'code_amount', 'code_length', 'can_use',  'use_times_limit',
        'has_date_limit', 'active_start', 'active_end', 'Package', 'Button', 'Codes',
    )

    def Package(self, obj):
        return u'<a href="/admin/package/package/{0}/">{1}</a>'.format(obj.package.id, obj.package.name)
    Package.allow_tags = True

    def _codes(self, obj):
        x = getattr(obj, '_cached_codes', None)
        if x:
            return x
        codes = obj.codes.all()
        x = [c.code_id for c in codes]
        obj._cached_codes = x
        return x

    def Codes(self, obj):
        text = self._codes(obj)
        return u"<br />".join(text)
    Codes.allow_tags = True

    def Button(self, obj):
        text = self._codes(obj)
        x = base64.urlsafe_b64encode(u'\n'.join(text))
        return '<a download="codes-{0}.txt" href="data:text/plain;base64,{1}">save</a> <a class="bucketbutton" href="#">show</a>'.format(obj.id, x)
    Button.allow_tags = True

    class Media:
        js = ('activatecode.js',)


class ActivateCodeUseLogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'code_id', 'char_id', 'Package', 'used_at'
    )

    def Package(self, obj):
        package = ActivateCode.objects.select_related('bucket', 'bucket__package').get(code_id=obj.code_id).bucket.package
        return u'<a href="/admin/package/package/{0}/">{1}</a>'.format(package.id, package.name)
    Package.allow_tags = True


admin.site.register(ActivateBucket, ActivateBucketAdmin)
admin.site.register(ActivateCodeUseLog, ActivateCodeUseLogAdmin)
