from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db import transaction
from django.contrib.auth import get_user_model

from .models import Activation
from .utils.email import send_activation_email, send_register_user_email


AuthUserModel = get_user_model()


@receiver(pre_save, sender=AuthUserModel)
def inactivate_user(instance, **kwargs):
    is_social_user = hasattr(instance, 'is_social_auth') and instance.is_social_auth is True
    if not instance.pk and not is_social_user:
        instance.is_active = False
        instance.password = None


@receiver(post_save, sender=AuthUserModel)
def create_activation(sender, instance, created, **kwargs):
    print('!!! Signal post_save was triggered!')
    is_social_user = hasattr(instance, 'is_social_auth') and instance.is_social_auth is True
    try:
        with transaction.atomic():
            if created:
                if not is_social_user:
                    Activation(user=instance).save()
                    send_activation_email(instance)
                else:
                    send_register_user_email(instance)
                    print(f"Sending welcome email to: {instance.email}")
    except ValueError:
        AuthUserModel.objects.get(pk=instance.id).delete()
