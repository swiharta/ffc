from django.views.generic import View
from djpjax import PJAXResponseMixin
from crossslide.models import CrossSlideImage

class GoogleMapView(PJAXResponseMixin, View):
  template_name = "google-map.html"

  def get(self, request):
    return self.render_to_response({'my': 'context'})

class SplashView(PJAXResponseMixin, View):
  template_name = "splash.html"

  def get(self, request):
#    images = CrossSlideImage.objects.all()
#    image0 = images[0]
    return self.render_to_response({'my': 'context',})# 'images': images,
#                                    'image0': image0})