import string
import random

from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives


# Email Functions

# Sends an email when a user registers to the website
def send_register_user_email(user_name, user_email):
    context = {
        "name": user_name,
        "email": user_email,
    }

    template = get_template("website/email/register_user_email.html")
    content = template.render(context)

    mail = EmailMultiAlternatives(
        subject=f"{user_name}, welcome to our website!",
        body=content,
        from_email=settings.EMAIL_HOST_USER,
        to=[user_email],
    )
    mail.content_subtype = "html"
    mail.send()


# Sends an email when a user hasn't logged in a long time
def send_login_user_email(user_name, user_email):
    context = {
        "name": user_name,
        "email": user_email,
    }

    template = get_template("website/email/user_long_time_email.html")
    content = template.render(context)

    mail = EmailMultiAlternatives(
        subject=f"{user_name}, welcome to our website!",
        body=content,
        from_email=settings.EMAIL_HOST_USER,
        to=[user_email],
    )
    mail.content_subtype = "html"
    mail.send()


# Sends an email when a user subscribes to the newsletter
def send_register_newsletter_email(sub_email):
    context = {
        "email": sub_email,
    }

    template = get_template("website/email/register_newsletter_email.html")
    content = template.render(context)

    mail = EmailMultiAlternatives(
        subject="Thank you for subscribing to our newsletter!",
        body=content,
        from_email=settings.EMAIL_HOST_USER,
        to=[sub_email],
    )
    mail.content_subtype = "html"
    mail.send()


# Utility

class RandomGenerator:
    """Random String Generator. Default length is 10 characters."""
    def __init__(self, length=10):
        self.length = length

    def random_string(self):
        char_list = string.ascii_lowercase + string.digits
        random_key = "".join(random.choices(char_list, k=self.length))

        return random_key

    def random_digits(self):
        char_list = string.digits
        random_key = "".join(random.choices(char_list, k=self.length))

        return random_key

    def random_letters(self):
        char_list = string.ascii_letters
        random_key = "".join(random.choices(char_list, k=self.length))

        return random_key


def generate_api_key():
    api_key = RandomGenerator(38).random_string()

    return api_key
