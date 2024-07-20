from .base import *

DEBUG = False

ALLOWED_HOSTS = ["seonghun.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgrestestdb",
        "USER": "myuser",
        "PASSWORD": "1q2w3e4r",
        "HOST": "postgres",
        "PORT": 5432,
    }
}

# celery
CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
