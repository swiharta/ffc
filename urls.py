from django.conf.urls.defaults import patterns, include, url

from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ffc.views.home', name='home'),
    # url(r'^ffc/', include('ffc.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^api/v1/', include('fiber.api.urls')),
	url(r'^admin/fiber/', include('fiber.admin_urls')),
	url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': ('fiber',),}),
	
	url(r'^', include('zinnia.urls.capabilities')),
	url(r'^search/', include('zinnia.urls.search')),
	url(r'^sitemap/', include('zinnia.urls.sitemap')),
	url(r'^trackback/', include('zinnia.urls.trackback')),
	url(r'^weblog/tags/', include('zinnia.urls.tags')),
	url(r'^weblog/feeds/', include('zinnia.urls.feeds')),
	url(r'^weblog/authors/', include('zinnia.urls.authors')),
	url(r'^weblog/categories/', include('zinnia.urls.categories')),
	url(r'^weblog/discussions/', include('zinnia.urls.discussions')),
	url(r'^weblog/', include('zinnia.urls.quick_entry')),
	url(r'^weblog/', include('zinnia.urls.entries')),
	url(r'^comments/', include('django.contrib.comments.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns('staticfiles.views',
		url(r'^site_media/static/(?P<path>.*)$', 'serve'),
		url(r'^site_media/media/(?P<path>.*)$', 'serve', {
			'document_root': settings.MEDIA_ROOT,
		}),
	)