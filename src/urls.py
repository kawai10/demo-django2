from django.apps import apps
from django.contrib import admin
from django.urls import path, include

from src import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("src.users.urls")),
    path("health", api.health_check, name="health-check"),
]

if apps.is_installed("debug_toolbar"):
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
