from .settings import *

import os
import dj_database_url
from decouple import config

DEBUG = config('DEBUG', cast=bool, default=False)

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['Faithbuildersv2.onrender.com']

# Database config
DATABASES = {
    'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        default='postgresql://postgres:postgres@localhost:5432/mysite',
        conn_max_age=600
    )
}
# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# CSRF & Secure settings
CSRF_TRUSTED_ORIGINS = ['https://Faithbuildersv2.onrender.com']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Optional Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
