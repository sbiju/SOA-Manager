###### Coding For Entrepreneur Guide #######

import os
from django.conf import settings

DEBUG = True
TEMPLATE_DEBUG = True

SECRET_KEY = '!76fwtfe+ot%w!hjd1(bz64j8m#t6qw0p(3@j1b4k1uz0ggpj8'
DATABASES = settings.DATABASES

''' Try lang ni
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'project_soa',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '',
        'PORT': '',
    }
}
'''

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'







