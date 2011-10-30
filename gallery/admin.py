from django.contrib import admin

from zinnia.models import Entry
from zinnia.admin import EntryAdmin
from gallery.models import EntryImage

class EntryImageInline(admin.TabularInline):
    model = EntryImage

class EntryAdminImage(EntryAdmin):
    inlines = (EntryImageInline,)

admin.site.unregister(Entry)
admin.site.register(Entry, EntryAdminImage)