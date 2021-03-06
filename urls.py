# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.defaults import patterns, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic.simple import redirect_to

urlpatterns = patterns('',
    # admin interface
    (r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^$', redirect_to, {'url': settings.BASE_URL + 'talk/new'}),
    (r'^talk/', include('manager.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
