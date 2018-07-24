"""
Django settings for ehw_io_public project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import uuid

import xblog.xmlrpc_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', str(uuid.uuid1()))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'True').lower() in ['true', 'yes', '1']
ALLOWED_HOSTS = os.environ.get('DJANGO_HOSTNAMES', '*').split()

XMLRPC_METHODS = []
XMLRPC_METHODS.extend(xblog.xmlrpc_settings.XMLRPC_METHODS)

MANAGERS = os.environ.get('MANAGERS', 'admin@ehw.io').split()
ADMINS = os.environ.get('ADMINS', 'admin@ehw.io').split()
# Application definition
if os.environ.get('CUMULUS_USERNAME'):
    CUMULUS = {
        'USERNAME': os.environ.get('CUMULUS_USERNAME'),
        'API_KEY': os.environ.get('CUMULUS_PASSWORD'),
        'CONTAINER': os.environ.get('CUMULUS_CONTAINER', 'my-media-container'),
        'STATIC_CONTAINER': os.environ.get('CUMULUS_STATIC_CONTAINER',
                                           'my-static-container'),
        'REGION': os.environ.get('CUMULUS_REGION', 'DFW'),
        'PYRAX_IDENTITY_TYPE': 'rackspace',
        'USE_PYRAX': True,
        'USE_SSL': True,
        'SERVICENET': False,
    }
    DEFAULT_FILE_STORAGE = 'cumulus.storage.SwiftclientStorage'
    STATICFILES_STORAGE = 'cumulus.storage.SwiftclientStaticStorage'

if os.environ.get('AWS_STORAGE_BUCKET_NAME'):
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = os.environ.get('AWS_S3_CUSTOM_DOMAIN')
    STATIC_URL = os.environ.get('STATIC_URL')
    STATICFILES_STORAGE = os.environ.get('STATICFILES_STORAGE')
    DEFAULT_FILE_STORAGE = os.environ.get('STATICFILES_STORAGE')
    AWS_IS_GZIPPED = True
    MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'ehw_io_static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticroot')
STATIC_URL = '/static/'


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'storages',
    'haystack',
    'django_xmlrpc',
    'markdown_deux',
    'bootstrap3',
    'xblog',
    'social_django',
    'ehwio'
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


SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'xblog.pipeline.debug',
    'social.pipeline.social_auth.social_uid',
    'xblog.pipeline.debug',
    'social.pipeline.social_auth.auth_allowed',
    'xblog.pipeline.debug',
    'social.pipeline.social_auth.social_user',
    'xblog.pipeline.debug',
    'social.pipeline.user.get_username',
    'xblog.pipeline.debug',
    'social.pipeline.user.create_user',
    'xblog.pipeline.debug',
    'social.pipeline.social_auth.associate_user',
    'xblog.pipeline.debug',
    'social.pipeline.social_auth.load_extra_data',
    'xblog.pipeline.debug',
    'social.pipeline.user.user_details',
    'xblog.pipeline.debug',
    'xblog.pipeline.update_user_social_data',
    'xblog.pipeline.debug',
    'xblog.pipeline.create_user_blog',
)

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DJANGO_DB_ENGINE',
                                 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('DJANGO_DB_NAME',
                               os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': os.environ.get('DJANGO_DB_USER'),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD'),
        'HOST': os.environ.get('DJANGO_DB_HOST'),
        'PORT': os.environ.get('DJANGO_DB_PORT')
    }
}

LANGUAGE_CODE = os.environ.get('DJANGO_LANG', 'en-us')
TIME_ZONE = os.environ.get('DJANGO_TIMEZONE', 'UTC')
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
# TEMPLATE_DIRS=(os.environ.get("DJANGO_TEMPLATE_DIR"),
# os.path.join(BASE_DIR, "templates"),)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.environ.get('DJANGO_TEMPLATE_DIR'), 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media'
            ],
        },
    },
]


STATIC_URL = os.environ.get('DJANGO_STATIC_URL', '/static/')
SITE_ID = os.environ.get('DJANGO_SITE_ID', 1)


# check to see if the user has created a cumulus user

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# the rest of this could probably be factored out...
MARKDOWN_DEUX_STYLES = {
    # default style
    'default': {
        'default': {
            'extras': {'code-friendly': None},
            'safe_mode': 'escape'
        }
    },
    'flatpages' : {
        'extras': {
            'footnotes': None,
        }
    }
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE':
            os.environ.get('DJANGO_HAYSTACK_ENGINE',
                           'haystack.backends.whoosh_backend.WhooshEngine'),
        'PATH':
            os.environ.get('DJANGO_HAYSTACK_PATH',
                           os.path.join(os.path.dirname(__file__),
                                        'whoosh_index')),
    },
}

if os.environ.get('DJANGO_HAYSTACK_URL'):
    HAYSTACK_CONNECTIONS['default']['URL'] = \
        os.environ.get('DJANGO_HAYSTACK_URL')

if os.environ.get('DJANGO_HAYSTACK_INDEX_NAME'):
    HAYSTACK_CONNECTIONS['default']['INDEX_NAME'] = \
        os.environ.get('DJANGO_HAYSTACK_INDEX_NAME')


CACHES = {
    'default': {
        'BACKEND':
            os.environ.get('DJANGO_CACHE_BACKEND',
                           'django.core.cache.backends.locmem.LocMemCache'),
        'LOCATION':
            os.environ.get('DJANGO_CACHE_LOCATION',
                           '/tmp/django_cache/'),
        'TIMEOUT':
            os.environ.get('DJANGO_CACHE_TIMEOUT', 1),
    }
}

EMAIL_HOST = os.environ.get('DJANGO_EMAIL_HOST', 'localhost')
EMAIL_PORT = os.environ.get('DJANGO_EMAIL_PORT', '25')

AUTHENTICATION_BACKENDS = (
    # 'social.backends.open_id.OpenIdAuth',
    # 'social.backends.google.GoogleOpenId',
    # 'social.backends.google.GoogleOAuth2',
    # 'social.backends.google.GoogleOAuth',
    'social.backends.twitter.TwitterOAuth',
    # 'social.backends.yahoo.YahooOpenId',
    'django.contrib.auth.backends.ModelBackend',
)
DEFAULT_FROM_EMAIL = \
    os.environ.get('DJANGO_FROM_EMAIL', 'Helpdesk <helpdesk@ehw.io>')
SOCIAL_AUTH_URL_NAMESPACE = \
    os.environ.get('DJANGO_SOCIAL_AUTH_URL_NAMESPACE', 'social')
SOCIAL_AUTH_TWITTER_KEY = \
    os.environ.get('DJANGO_SOCIAL_AUTH_TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET = \
    os.environ.get('DJANGO_SOCIAL_AUTH_TWITTER_SECRET')

# all that loggin'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
            'formatter': 'verbose',
        },
        'requestfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'request-debug.log'),
            'formatter': 'verbose',
        },
        'xblog_handler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'xblog.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':DEBUG and 'DEBUG' or 'INFO',
        },
        'xblog': {
            'handlers': ['xblog_handler'],
            'level': DEBUG and 'DEBUG' or 'INFO',
        },
        'django.request': {
            'handlers': ['requestfile'],
            'level': DEBUG and 'DEBUG' or 'INFO',
            'propagate': True,
        },
        'xmlrpc': {
            'handlers': ['xblog_handler',],
            'level' : DEBUG and 'DEBUG' or 'INFO',
            'propagate' : True,
        }

    },
    'formatters': {
        'verbose': {
            'format' : '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt' : '%d/%b/%Y %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
}
