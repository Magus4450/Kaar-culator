from lib2to3.pgen2 import grammar
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as BaseUserManager



"""
    Since we are using Django's built-in User model and we are not using 'username' field to login or register,
    we need to override the default UserManager to use email instead of username for validations.
"""
class UserManager(BaseUserManager):
    """ User Manager that knows how to create users via email instead of username """
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"
    username = models.CharField(('username'), max_length=30, blank=True)
    email = models.EmailField("Email", blank=False, null=False, unique=True)
    objects = UserManager()
    groups = None
    user_permissions = None


class UserInfo(models.Model):

    # Extra fields
    pass
