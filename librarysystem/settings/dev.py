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