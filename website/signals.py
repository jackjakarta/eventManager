from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile, NewsletterSub

AuthUser = get_user_model()


@receiver(post_save, sender=AuthUser)
def create_profile(sender, instance, created, **kwargs):
    print("\nSignals post_save was caught!")
    if created:
        Profile(user=instance).save()
        print("Created profile successfully!")


@receiver(post_save, sender=AuthUser)
def add_newsletter(sender, instance, created, **kwargs):
    print("\nSignals post_save was caught!")
    if created:
        if not NewsletterSub.objects.filter(email=instance).exists():
            NewsletterSub(email=instance).save()
            print("User added to newsletter list!")
