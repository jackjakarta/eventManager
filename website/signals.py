from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile, NewsletterSub
# from .utils import send_register_newsletter_email, send_register_user_email

AuthUser = get_user_model()


@receiver(post_save, sender=AuthUser)
def create_profile(sender, instance, created, **kwargs):
    print("\nSignals post_save was caught!")
    if created:
        Profile(user=instance).save()
        print("Created profile successfully!")


# @receiver(post_save, sender=AuthUser)
# def send_registered_user_email(sender, instance, created, **kwargs):
#     print("\nSignal post_save was caught!")
#     if created:
#         send_register_user_email(user_name=instance.first_name, user_email=instance.email)
#         print("Email sent successfully!")


@receiver(post_save, sender=AuthUser)
def add_newsletter(sender, instance, created, **kwargs):
    print("\nSignals post_save was caught!")
    if created:
        if not NewsletterSub.objects.filter(email=instance).exists():
            NewsletterSub(email=instance).save()
            print("User added to newsletter list!")
