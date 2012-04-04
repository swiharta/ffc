from django.conf.urls.defaults import patterns, include, url

from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template, redirect_to
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', direct_to_template, {'template': 'ffc_home.html'}, name="home"),
  url(r"^robots\.txt$", direct_to_template, {
    "template": "robots.txt", 'mimetype': 'text/plain'}, ),
  (r'^favicon\.ico$', redirect_to, {
    'url': '/site_media/static/images/favicon.ico'}),
#  url(r'^ffc/', include('ffc.foo.urls')),

  url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
  url(r'^admin/', include(admin.site.urls)),
#	url(r'^api/v1/', include('fiber.api.urls')),
#	url(r'^admin/fiber/', include('fiber.admin_urls')),
#	url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': ('fiber',),}),

  url(r'^', include('zinnia.urls.capabilities')),
  url(r'^search/', include('zinnia.urls.search')),
  url(r'^sitemap/', include('zinnia.urls.sitemap')),
  url(r'^trackback/', include('zinnia.urls.trackback')),
  url(r'^news/tags/', include('zinnia.urls.tags')),
  url(r'^news/feeds/', include('zinnia.urls.feeds')),
  url(r'^news/authors/', include('zinnia.urls.authors')),
  url(r'^news/categories/', include('zinnia.urls.categories')),
  url(r'^news/discussions/', include('zinnia.urls.discussions')),
  url(r'^news/', include('zinnia.urls.quick_entry')),
  url(r'^news/', include('zinnia.urls.entries')),
  url(r'^comments/', include('django.contrib.comments.urls')),

#  url(r'^tinymce/', include('tinymce.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns('staticfiles.views',
		url(r'^site_media/static/(?P<path>.*)$', 'serve'),
		url(r'^site_media/media/(?P<path>.*)$', 'serve', {
			'document_root': settings.MEDIA_ROOT,
		}),
	)