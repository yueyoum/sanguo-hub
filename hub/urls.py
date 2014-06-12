from django.conf.urls import patterns, include, url
from django.conf import settings

import cron

if settings.ENABLE_ADMIN:
    from django.contrib import admin
    admin.autodiscover()

    urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    )

else:
    urlpatterns = patterns('',
        url(r'', include('views.urls')),
    )
