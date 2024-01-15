from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile, APIKey, NewsletterSub
from .utils import generate_api_key

AuthUser = get_user_model()


@receiver(post_save, sender=AuthUser)
def create_profile(sender, instance, created, **kwargs):
    print("\nSignals post_save was caught!\n")
    if created:
        print("Created profile successfully!")
        Profile(user=instance).save()


@receiver(post_save, sender=AuthUser)
def create_api_key(sender, instance, created, **kwargs):
    print("\nSignals post_save was caught!\n")
    if created:
        print("Generated API Key successfully!")
        api_key = generate_api_key()
        APIKey(user=instance, api_key=api_key).save()


@receiver(post_save, sender=AuthUser)
def add_newsletter(sender, instance, created, **kwargs):
    print("\nSignals post_save was caught!\n")
    if created:
        print("User added to newsletter list!")
        NewsletterSub(email=instance).save()
