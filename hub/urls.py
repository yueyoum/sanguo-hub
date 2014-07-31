from django.conf.urls import patterns, include, url
from django.conf import settings

if settings.ENABLE_ADMIN:
    from django.contrib import admin
    admin.autodiscover()

    from status.views import StatusView

    urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^status/$', StatusView.as_view()),
    )

else:
    urlpatterns = patterns('',
        url(r'', include('views.urls')),
    )
