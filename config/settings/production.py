from .base import *

DEBUG = False

ALLOWED_HOSTS = ["seonghun.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB", default="postgres"),
        "USER": env("POSTGRES_USER", default="myuser"),
        "PASSWORD": env("POSTGRES_PASSWORD", default="1q2w3e4r"),
        "HOST": env("POSTGRES_HOST", default="postgres"),
        "PORT": env("POSTGRES_PORT", default=5432),
    }
}

# celery
CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
