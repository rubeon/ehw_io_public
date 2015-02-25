"""
Django settings for ehw_io_public project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = os.environ.get("DJANGO_HOSTNAMES", 'localhost 127.0.0.1').split()


# Application definition

CUMULUS = {
    'USERNAME': os.environ.get("CUMULUS_USERNAME"),
    'API_KEY': os.environ.get("CUMULUS_PASSWORD"),
    'CONTAINER': os.environ.get('CUMULUS_CONTAINER', 'my-media-container'),
    'STATIC_CONTAINER': os.environ.get('CUMULUS_STATIC_CONTAINER', 'my-static-container'),
    'REGION': os.environ.get("CUMULUS_REGION", "DFW"),
    'PYRAX_IDENTITY_TYPE': 'rackspace',
    'USE_PYRAX': True,
    'USE_SSL': True,
    'SERVICENET': True,
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'cumulus',
    'haystack',
    'django_xmlrpc',
    'tinylinks',
    'markdown_deux',
    'bootstrap3',
    'xblog',
    'social.apps.django_app.default',
    'django_libs'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ehw_io_public.urls'

WSGI_APPLICATION = 'ehw_io_public.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# 

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DJANGO_DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('DJANGO_DB_NAME', os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': os.environ.get('DJANGO_DB_USER'),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD'),
        'HOST': os.environ.get('DJANGO_DB_HOST'),
        'PORT': os.environ.get('DJANGO_DB_PORT')
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = os.environ.get("DJANGO_LANG", "en-us")
TIME_ZONE = os.environ.get("DJANGO_TIMEZONE", "UTC")
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
TEMPLATE_DIRS=(os.environ.get("DJANGO_TEMPLATE_DIR"), os.path.join(BASE_DIR, "templates"),)
STATIC_URL = os.environ.get("DJANGO_STATIC_URL",'/static/')
SITE_ID = os.environ.get("DJANGO_SITE_ID")

XMLRPC_METHODS = (
    ('xblog.metaWeblog.blogger_deletePost', 'blogger.deletePost'),
    ('xblog.metaWeblog.blogger_getRecentPosts', 'blogger.getRecentPosts'),
    ('xblog.metaWeblog.blogger_getUserInfo', 'blogger.getUserInfo'),
    ('xblog.metaWeblog.blogger_getUsersBlogs', 'blogger.getUsersBlogs'),
    ('xblog.metaWeblog.wp_getUsersBlogs', 'wp.getUsersBlogs'),
    ('xblog.metaWeblog.wp_getOptions', 'wp.getOptions'),
    ('xblog.metaWeblog.metaWeblog_editPost', 'metaWeblog.editPost'),
    ('xblog.metaWeblog.metaWeblog_getCategories', 'metaWeblog.getCategories'),
    ('xblog.metaWeblog.metaWeblog_getPost', 'metaWeblog.getPost'),
    ('xblog.metaWeblog.metaWeblog_getRecentPosts', 'metaWeblog.getRecentPosts'),
    ('xblog.metaWeblog.metaWeblog_getUsersBlogs', 'metaWeblog.getUsersBlogs'),
    ('xblog.metaWeblog.metaWeblog_newMediaObject', 'metaWeblog.newMediaObject'),
    ('xblog.metaWeblog.metaWeblog_newPost', 'metaWeblog.newPost'),
    ('xblog.metaWeblog.mt_getCategoryList', 'mt.getCategoryList'),
    ('xblog.metaWeblog.mt_getPostCategories', 'mt.getPostCategories'),
    ('xblog.metaWeblog.mt_publishPost', 'mt.publishPost'),
    ('xblog.metaWeblog.mt_setPostCategories', 'mt.setPostCategories'),
    ('xblog.metaWeblog.mt_supportedMethods', 'mt.supportedMethods'),
    ('xblog.metaWeblog.mt_supportedTextFilters', 'mt.supportedTextFilters'),
    ('xblog.metaWeblog.wp_getUsersBlogs', 'wp.getUsersBlogs'),
    ('xblog.metaWeblog.wp_getOptions', 'wp.getOptions'),
    ('xblog.metaWeblog.wp_getTags', 'wp.getTags'),
)


# check to see if the user has created a cumulus user
if CUMULUS['USERNAME']:
    DEFAULT_FILE_STORAGE = 'cumulus.storage.SwiftclientStorage'
    STATICFILES_STORAGE = 'cumulus.storage.SwiftclientStaticStorage'
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
# )
STATIC_ROOT =   os.path.join(BASE_DIR, "static")

# the rest of this could probably be factored out...
MARKDOWN_DEUX_STYLES = {
    # default style
    "default": {'default': {'extras': {'code-friendly': None}, 'safe_mode': 'escape'}},
    "flatpages" : {
        'extras': {
            "footnotes": None,
        }
    }
}
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': os.environ.get('DJANGO_HAYSTACK_ENGINE', 'haystack.backends.whoosh_backend.WhooshEngine'),
        'PATH': os.environ.get('DJANGO_HAYSTACK_PATH', os.path.join(os.path.dirname(__file__), 'whoosh_index')),
    },
}

CACHES = {
    'default': {
        'BACKEND':os.environ.get('DJANGO_CACHE_BACKEND', 'django.core.cache.backends.filebased.FileBasedCache'),
        'LOCATION': os.environ.get('DJANGO_CACHE_LOCATION', '/tmp/django_cache/')
    }
}

EMAIL_HOST = os.environ.get("DJANGO_EMAIL_HOST", "localhost")
EMAIL_PORT = os.environ.get("DJANGO_EMAIL_PORT", "25")

#FIXME: Add following to init env
AUTHENTICATION_BACKENDS = (
    # 'social.backends.open_id.OpenIdAuth',
    # 'social.backends.google.GoogleOpenId',
    # 'social.backends.google.GoogleOAuth2',
    # 'social.backends.google.GoogleOAuth',
    'social.backends.twitter.TwitterOAuth',
    # 'social.backends.yahoo.YahooOpenId',
    'django.contrib.auth.backends.ModelBackend',
)
DEFAULT_FROM_EMAIL = os.environ.get("DJANGO_FROM_EMAIL", "Helpdesk <helpdesk@ehw.io>")
SOCIAL_AUTH_URL_NAMESPACE = os.environ.get('DJANGO_SOCIAL_AUTH_URL_NAMESPACE', 'social')
SOCIAL_AUTH_TWITTER_KEY = os.environ.get('DJANGO_SOCIAL_AUTH_TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET = os.environ.get('DJANGO_SOCIAL_AUTH_TWITTER_SECRET')
