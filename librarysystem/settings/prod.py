import os
import dj_database_url
from .common import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': dj_database_url.config()
}

# EMAIL_USE_TLS = True
# EMAIL_HOST = os.environ['MAILGUN_SMTP_SERVER']
# EMAIL_HOST_USER = os.environ['MAILGUN_SMTP_LOGIN']
# EMAIL_HOST_PASSWORD = os.environ['MAILGUN_SMTP_PASSWORD']
# EMAIL_PORT = os.environ['MAILGUN_SMTP_PORT']

EMAIL_HOST = os.environ['CLOUDMAILIN_FORWARD_ADDRESS']
EMAIL_HOST_USER = os.environ['CLOUDMAILIN_USERNAME']
EMAIL_HOST_PASSWORD = os.environ['CLOUDMAILIN_PASSWORD']
EMAIL_PORT = 587

STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "static/"

 
 

 
 