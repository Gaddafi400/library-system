from .common import *
import cloudinary

DEBUG = True

SECRET_KEY = 'django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp'

 
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

 
ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = "static_root"


cloudinary.config( 
  cloud_name = "hinhddrry", 
  api_key = "185741933723892", 
  api_secret = "Ht68BBPELYuM-pvAutcPplFB0nE" 
)


# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# EMAIL_HOST = "smtp.mailgun.org"
# EMAIL_HOST_USER = "postmaster@sandbox1cdb6f25f3404768898598de45897291.mailgun.org"
# EMAIL_HOST_PASSWORD = "24bf552a9b2d0f1d043143d60d8b4cdc-48c092ba-750df0f9"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "adamugaddafi99@gmail.com"
EMAIL_HOST_PASSWORD = "rkrtbxsuunhgzdlx"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# rkrtbxsuunhgzdlx

