from django.apps import apps
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("src.users.urls")),
]

if apps.is_installed("debug_toolbar"):
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
