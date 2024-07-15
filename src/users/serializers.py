from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    AuthUser,
    TokenRefreshSerializer,
)
from rest_framework_simplejwt.tokens import Token

from src.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    @staticmethod
    def get_all_users():
        return User.objects.all()


class CreateUserSerializer(UserSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            name=validated_data["name"],
        )
        return user


class LoginSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user: AuthUser) -> Token:
        token = super().get_token(user)

        token["email"] = user.email
        token["name"] = user.name
        return token
