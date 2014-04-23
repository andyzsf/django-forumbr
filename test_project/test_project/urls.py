from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^forum/', include('forum.urls', namespace='forum')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
