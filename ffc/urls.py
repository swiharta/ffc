from django.conf.urls import include, url

from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
# from django.views.generic.simple import direct_to_template, redirect_to
from main.views import SplashView, GoogleMapView

urlpatterns = [
  url(r'^$', SplashView.as_view(), name="home"),
  url(r'^map/', GoogleMapView.as_view(), name="map"),
#  url(r'^$', direct_to_template, {'template': 'ffc-home.html'}, name="home"),
#   url(r"^robots\.txt$", direct_to_template, {
#     "template": "robots.txt", 'mimetype': 'text/plain'}, ),
#   (r'^favicon\.ico$', redirect_to, {
#     'url': '/site_media/static/images/favicon.ico'}),
#  url(r'^ffc/', include('ffc.foo.urls')),

  url(r'^admin/', include(admin.site.urls)),

#  url(r'^tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
