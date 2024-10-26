from secrets import token_urlsafe

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework_api_key.models import AbstractAPIKey

from .managers import AuthUserManager
from .utils.constants import ACTIVATION_AVAILABILITY


class AuthUser(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="email", max_length=255, unique=True)
    password = models.CharField(_("password"), max_length=128, null=True, blank=False)
    is_newsletter_sub = models.BooleanField(
        verbose_name="Newsletter Sub",
        default=False,
        help_text=_("Check box if you want to subscribe to the newsletter."),
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = AuthUserManager()

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.__str__()


AVAILABILITY = {ACTIVATION_AVAILABILITY["unit"]: ACTIVATION_AVAILABILITY["value"]}


class Activation(models.Model):
    user = models.OneToOneField(
        AuthUser, related_name="activation", on_delete=models.CASCADE
    )
    token = models.CharField(
        max_length=64,
        null=True,
        unique=True,
        default=None,
    )
    expires_at = models.DateTimeField(default=None)
    activated_at = models.DateTimeField(default=None, null=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = token_urlsafe(32)
            self.expires_at = timezone.now() + timezone.timedelta(**AVAILABILITY)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.user)

    def __repr__(self):
        return f"{self.user} - {self.token}"


class UserAPIKey(AbstractAPIKey):
    user = models.ForeignKey(
        AuthUser, on_delete=models.CASCADE, related_name="api_keys"
    )
