from django.db import models
from django.utils.translation import ugettext_lazy as _

class CrossSlideImage(models.Model):
#  entry = models.ForeignKey(Entry, verbose_name=_('entry'))
  image = models.ImageField(_('image'), upload_to='media/images')
  title = models.CharField(_('title'), max_length=250, blank=True, null=True)
  description = models.TextField(_('description'), blank=True, null=True)
  from_data = models.CharField(_('"from" data'), max_length=20, blank=True, null=True)
  to_data = models.CharField(_('"to" data'), max_length=20, blank=True, null=True)
  time = models.IntegerField(_('time to display in seconds'), blank=True, null=True)

  def __unicode__(self):
    return self.title