from django.contrib import admin

from cross_slide.models import CrossSlideImage

class CrossSlideImageAdmin(admin.ModelAdmin):
    model = CrossSlideImage

admin.site.register(CrossSlideImage, CrossSlideImageAdmin)