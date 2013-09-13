# coding: utf-8
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from zinnia.models.entry import Entry
from zinnia.admin.entry import EntryAdmin


class CustomEntryAdmin(EntryAdmin):
    # Add audio to Content
    # Move slug from Publication to Content
    fieldsets = \
        ((_('Content'), {'fields': ('title', 'content', 'image', 'status', 'audio', 'slug')}),) + \
        EntryAdmin.fieldsets[1:-1] + \
        ((_('Publication'), {'fields': ('categories', 'tags', 'sites')}),)


admin.site.unregister(Entry)
admin.site.register(Entry, CustomEntryAdmin)
