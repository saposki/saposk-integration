from settings import BASE_DIR, ROOT_URLCONF
import os

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'saposki',
        'USER': 'saposkiuser',
        'PASSWORD': 'sappskipassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
