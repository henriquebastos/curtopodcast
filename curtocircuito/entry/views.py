# coding: utf-8
from django.views.generic.detail import DetailView
from zinnia.models.entry import Entry
from zinnia.views.mixins.entry_protection import EntryProtectionMixin


class EntryDetail(EntryProtectionMixin, DetailView):
    queryset = Entry.published.on_site()
    template_name_field = 'template'
