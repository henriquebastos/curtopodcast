from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^atom.xml$', 'curtocircuito.core.views.atom', name='atom'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include('curtocircuito.entry.urls')),
    url(r'^', include('curtocircuito.core.sitemaps_urls')),
)
