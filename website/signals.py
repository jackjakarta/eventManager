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
def register_user_newsletter(sender, instance, created, **kwargs):
    print("\nSignals post_save was caught!")
    if created:
        if instance.is_newsletter_sub:
            if not NewsletterSub.objects.filter(email=instance).exists():
                NewsletterSub(email=instance).save()
                print("User added to newsletter list!")


@receiver(post_save, sender=AuthUser)
def add_user_to_newsletter(sender, instance, **kwargs):
    print("\nSignals post_save was caught!")
    if instance.is_newsletter_sub:
        if not NewsletterSub.objects.filter(email=instance).exists():
            NewsletterSub(email=instance).save()
            print("User added to newsletter list.")


# @receiver(post_save, sender=AuthUser)
# def remove_user_from_newsletter(sender, instance, **kwargs):
#     print("\nSignals post_save was caught!")
#     if not instance.is_newsletter_sub:
#         if NewsletterSub.objects.filter(email=instance).exists():
#             NewsletterSub(email=instance).delete()
#             print("User removed from newsletter list.")


@receiver(post_save, sender=AuthUser)
def remove_user_from_newsletter(sender, instance, **kwargs):
    print("\nSignals post_save was caught!")
    if not instance.is_newsletter_sub:
        newsletter_subs = NewsletterSub.objects.filter(email=instance)
        if newsletter_subs.exists():
            newsletter_subs.delete()
            print("User removed from newsletter list.")
