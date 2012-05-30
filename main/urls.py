from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
from main.views import GoogleMapView, SplashView
from django.views.generic.simple import direct_to_template, redirect_to

#urlpatterns = patterns('',
#  url(r'^map/', GoogleMapView.as_view(), name="map"),
#  url(r'^splash/', SplashView.as_view(), name="splash"),
#                      )