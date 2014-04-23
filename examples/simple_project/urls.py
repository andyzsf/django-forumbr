from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.shortcuts import redirect

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', lambda req: redirect('/forum/')),
    url(r'^forum/', include('forum.urls', namespace='forum')),
    url(r'^auth/', include('registration.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'serve',
        {'document_root': settings.MEDIA_ROOT}),
    )
