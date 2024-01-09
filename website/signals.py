from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile, NewsletterSub

AuthUser = get_user_model()


@receiver(post_save, sender=AuthUser)
def create_profile(sender, instance, created, **kwargs):
    print("\nSignals post_save was caught!\n")
    if created:
        print("Created profile successfully")
        Profile(user=instance).save()


@receiver(post_save, sender=AuthUser)
def add_newsletter(sender, instance, created, **kwargs):
    print("\nSignals post_save was caught!\n")
    if created:
        print("User added to newsletter list.")
        NewsletterSub(email=instance).save()
