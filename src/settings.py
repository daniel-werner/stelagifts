# Django settings for stellagifts project.
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'stelagifts',                      # Or path to database file if using sqlite3.
        'USER': 'vernerd',                      # Not used with sqlite3.
        'PASSWORD': 'sw6PhaSw',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}

CACHE_BACKEND = 'db://cache'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = None

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'hu'
ADMIN_LANGUAGE_CODE = 'en'

DEFAULT_LANGUAGE = 1

#gettext = lambda s: s
LANGUAGES = (
    ('hu', 'Magyar'),
    ('sr', 'Srpski'),    
    ('en', 'English'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

import os
HTTP_ROOT = os.path.dirname(__file__)

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = HTTP_ROOT + '/../static/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://static.stelagifts.co.cc/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = 'http://static.stelagifts.co.cc/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '%w+r79=c%q)omompz*ms8t$y1a@5_ngc5k2)v7*0-fib@2fknm'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
    'middleware.AdminLocaleURLMiddleware',    
    'localeurl.middleware.LocaleURLMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',        
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'multilingual.flatpages.middleware.FlatpageFallbackMiddleware',
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'breadcrumbs.middleware.BreadcrumbsMiddleware',
    'breadcrumbs.middleware.FlatpageFallbackMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',    
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'multilingual.context_processors.multilingual',
    'django.core.context_processors.request',    
    'context_processors.media_url',
)

INTERNAL_IPS=('127.0.0.1')

ROOT_URLCONF = 'urls'

import re
LOCALE_INDEPENDENT_PATHS = (
    re.compile('^/admin/'),
    re.compile('^/ckeditor/'),    
)

LOCALE_INDEPENDENT_MEDIA_URL = True

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    HTTP_ROOT + "/templates",
    HTTP_ROOT + "/ckeditor/templates"
)

CKEDITOR_MEDIA_PREFIX = "http://static.stelagifts.co.cc/media/ckeditor/"
CKEDITOR_UPLOAD_PATH = HTTP_ROOT + "/../static/uploads"

CKEDITOR_CONFIGS = {
           'default': {
               'toolbar': 'Basic',
           },
           'full_ckeditor': {
               'toolbar': 'Full',
               'width' : 960,
               'height' : 300
           },           
       }

BREADCRUMBS_AUTO_HOME = True
ASSETS_DEBUG = False
CAPTCHA_NOISE_FUNCTIONS=('captcha.helpers.noise_dots',)
CAPTCHA_FONT_SIZE=55
CAPTCHA_LENGTH=5
CAPTCHA_TIMEOUT=15

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',                  
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'products',
    'sorl.thumbnail',
    'multilingual',
    'multilingual.flatpages',
    'localeurl',
    'django_assets',
    'contact',
    'captcha'
    #'tagging'
    #'breadcrumbs'
    #'django.contrib.flatpages'
)
