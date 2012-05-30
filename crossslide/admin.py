from django.contrib import admin

from crossslide.models import CrossSlideImage

class CrossSlideImageAdmin(admin.ModelAdmin):
    model = CrossSlideImage

admin.site.register(CrossSlideImage, CrossSlideImageAdmin)