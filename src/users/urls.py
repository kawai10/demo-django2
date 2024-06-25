from django.urls import path, include

from src.users import api

app_name = "users"

urlpatterns = [
    path("signup", api.RegisterUserAPIView.as_view(), name="user-signup"),
    path("login", api.LoginUserAPIView.as_view(), name="user-login"),
    path("refresh", api.TokenRefreshAPIView.as_view(), name="user-refresh"),
]
