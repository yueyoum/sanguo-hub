from django.conf.urls import patterns, include, url
from django.conf import settings

if settings.ENABLE_ADMIN:
    from django.contrib import admin
    admin.autodiscover()

    urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    )

else:
    urlpatterns = patterns('',
        # Examples:
        # url(r'^$', 'gate.views.home', name='home'),
        # url(r'^blog/', include('blog.urls')),

        # url(r'^admin/', include(admin.site.urls)),

        url(r'', include('views.urls')),
    )
