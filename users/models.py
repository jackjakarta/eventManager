from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import AuthUserManager


class AuthUser(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name="email",
        max_length=255,
        unique=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = AuthUserManager()

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.__str__()
