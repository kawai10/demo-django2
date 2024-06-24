from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):

    def create_user(self, email, name, password):
        if not email:
            raise ValueError("Users must have an email address")
        if not name:
            raise ValueError("Users must have a name")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(
            email=self.normalize_email(email), name=name, password=password
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = CustomUserManager()

    class Meta:
        db_table = "users"

    email = models.EmailField(unique=True, max_length=255, verbose_name="email address")
    name = models.CharField(max_length=30, verbose_name="user name")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")
    is_active = models.BooleanField(default=True, verbose_name="is active")
    last_login = models.DateTimeField(auto_now=True, verbose_name="last login")

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS가 없는 경우 createsuperuser 명령어 시 email과 password만 입력함.
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_superuser and self.is_active
