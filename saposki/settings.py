"""
Django settings for saposki project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import datetime
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o+3%zf1%u(4tjer5u_%kkhb(n38q2xqs*soq$h4@j4*gpn2iq2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
    'about',
    'portrait',
    'crasher',
    'street',
    'storages',
    'boto',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'saposki.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'saposki.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

db = 'postgres://vendmkuzmsalwr:shgcYa2mat7dhvUyopSscYUcsx@ec2-54-243-249-176.compute-1.amazonaws.com:5432/d2p578kgndvb42'
DATABASES = { 'default' : dj_database_url.config(default=db)}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

access_key = 'AKIAJVESQIIMDC6IT5BA'
secret_key = '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'

AWS_ACCESS_KEY_ID = access_key
AWS_SECRET_ACCESS_KEY = secret_key

AWS_STORAGE_BUCKET_NAME = 'saposki'

STATICFILES_STORAGE = 'saposki.s3utils.StaticRootS3BotoStorage'
DEFAULT_FILE_STORAGE = 'saposki.s3utils.MediaRootS3BotoStorage'

S3_URL = '//%s.s3.amazonaws.com/' %AWS_STORAGE_BUCKET_NAME
MEDIA_URL = S3_URL + "media/"
STATIC_URL = S3_URL + "static/"
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

date_two_months_later = datetime.date.today() + datetime.timedelta(2 * 365 / 12)
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
    'Expires': expires,
    'Cache-Control': 'max-age=86400',
}


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # '/var/www/static/',
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")

# # Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# try to load local_settings.py if it exists
# try:
#   from local_settings import *
# except Exception as e:
#   DATABASES = { 'default' : dj_database_url.config(default=db)}
#   pass

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#     }
# }
