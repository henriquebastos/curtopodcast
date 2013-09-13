# coding: utf-8
from django.conf.urls import url, include, patterns
from zinnia.urls import _
from .views import EntryDetail


urlpatterns = patterns('',
    url(_(r'^feeds/'), include('zinnia.urls.feeds')),
    url(_(r'^tags/'), include('zinnia.urls.tags',)),
    url(_(r'^authors/'), include('zinnia.urls.authors')),
    url(_(r'^categories/'), include('zinnia.urls.categories')),
    url(_(r'^search/'), include('zinnia.urls.search')),
    url(_(r'^random/'), include('zinnia.urls.random')),
    url(_(r'^sitemap/'), include('zinnia.urls.sitemap')),
    url(_(r'^trackback/'), include('zinnia.urls.trackback')),
    url(_(r'^comments/'), include('zinnia.urls.comments')),

    url(r'^(?P<slug>[-\w]+)/$', EntryDetail.as_view(), name='zinnia_entry_detail'),

    url(r'^', include('zinnia.urls.archives')),
    url(r'^', include('zinnia.urls.shortlink')),
    url(r'^', include('zinnia.urls.quick_entry')),
    url(r'^', include('zinnia.urls.capabilities')),
)
