# coding: utf-8
from django.conf.urls import patterns, url
from zinnia.sitemaps import EntrySitemap


sitemaps = {
    'blog': EntrySitemap,
}

urlpatterns = patterns('django.contrib.sitemaps.views',
    url(r'^sitemap.xml$', 'index', {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),
)
