from django.db import models
from django.utils.translation import ugettext_lazy as _

from zinnia.models import Entry

class EntryImage(models.Model):
    """Image Model"""
    entry = models.ForeignKey(Entry, verbose_name=_('entry'))

    image = models.ImageField(_('image'), upload_to='uploads/gallery')
    title = models.CharField(_('title'), max_length=250)
    description = models.TextField(_('description'), blank=True)

    def __unicode__(self):
        return self.title