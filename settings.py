# Django settings for ffc project.

import os.path
import posixpath

DEBUG = False
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

ADMINS = (
	("Andrew Swihart", "andrew@andrewswihart.net"),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2", # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': "swihart_ffc",                       # Or path to database file if using sqlite3.
        'USER': 'swihart_ffc',                      # Not used with sqlite3.
        'PASSWORD': '3chick04',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = "US/Eastern"

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

INTERNAL_IPS = ( # for debug_toolbar
  "127.0.0.1",
)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT, "site_media", "media")
MEDIA_URL = "/site_media/media/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "site_media", "static")
STATIC_URL = "/site_media/static/"

STATICFILES_FINDERS = (
'staticfiles.finders.FileSystemFinder',
'staticfiles.finders.AppDirectoriesFinder',
#'staticfiles.finders.DefaultStorageFinder',
'compressor.finders.CompressorFinder',
)

ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

# Additional locations of static files
STATICFILES_DIRS = [
	os.path.join(PROJECT_ROOT, "media"),
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'cjqi$jhooy&5$1y#pv7)cl_@8f8virco+_(bj+9sjq^hb^g($2'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',

  'debug_toolbar.middleware.DebugToolbarMiddleware',
	
#	'fiber.middleware.ObfuscateEmailAddressMiddleware',
#	'fiber.middleware.AdminPageMiddleware',
#	'fiber.middleware.PageFallbackMiddleware',
)

ROOT_URLCONF = 'ffc.urls'

TEMPLATE_DIRS = (
	os.path.join(PROJECT_ROOT, "templates"),
)

TEMPLATE_CONTEXT_PROCESSORS = [
	"django.core.context_processors.auth",
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	"django.core.context_processors.request",
	"django.contrib.messages.context_processors.messages",
	
	"staticfiles.context_processors.static_url",
	
#	'fiber.context_processors.page_info',
	
	'zinnia.context_processors.version', # Optional
	'zinnia.context_processors.media',
]

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.comments', # for zinnia
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	#'django.contrib.staticfiles',
	'django.contrib.admin',
	'django.contrib.admindocs',
	
	"docutils",

	"south",
	"ajax_select",
	"imagekit",
	"django_extensions",
	"mptt",
#	"taggit",
  #"tinymce",
	#"taggit_autocomplete",
	#"taggit_templatetags",
#	"fiber",
#	"piston", # may need to an __init__.py to site-packages/piston
	"staticfiles",
	"compressor",
	"admin_tools",
	"uni_form",
	"zinnia",
	"tagging",
  "debug_toolbar",

  "gallery"
)

DEBUG_TOOLBAR_CONFIG = {
  "INTERCEPT_REDIRECTS": False,
}

try:
    from local_settings import *
except ImportError:
    pass