from django.db import models
from django.utils.translation import ugettext_lazy as _
from zinnia.models.entry import EntryAbstractClass
from curtocircuito.entry.helpers import drop_field

# Workaround
drop_field(EntryAbstractClass, 'slug')


class TimelessEntry(EntryAbstractClass):
    """
    Simple abstract entry model class.
    """
    slug = models.SlugField(_('slug'), max_length=255, unique=True, help_text=_("Used to build the entry's URL."))
    audio = models.URLField(blank=True, null=True)

    class Meta(EntryAbstractClass.Meta):
        """
        CoreEntry's meta informations.
        """
        abstract = True

    @models.permalink
    def get_absolute_url(self):
        """
        Builds and returns the entry's URL based on the slug.
        """
        return ('zinnia_entry_detail', (), {'slug': self.slug})
