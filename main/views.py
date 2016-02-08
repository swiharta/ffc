from django.views.generic import TemplateView
# from crossslide.models import CrossSlideImage

class GoogleMapView(TemplateView):
  template_name = "google-map.html"

class SplashView(TemplateView):
  template_name = "splash.html"
