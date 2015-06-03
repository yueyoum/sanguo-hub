from django.conf.urls import patterns, include, url
from django.conf import settings

if settings.ENABLE_ADMIN:
    from django.contrib import admin
    admin.autodiscover()

    import status.views

    urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^status/$', status.views.StatusView.as_view()),
    url(r'^status/ajax/$', status.views.status_ajax),
    )

else:
    urlpatterns = patterns('',
        url(r'', include('views.urls')),
    )
