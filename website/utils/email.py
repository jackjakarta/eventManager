from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


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


# Sends an email when a user subscribes to the newsletter
def send_register_user_email(first_name, last_name, to_email):
    context = {
        "first_name": first_name,
        "last_name": last_name,
        "email": to_email,
    }

    template = get_template("website/email/register_user_email.html")
    content = template.render(context)

    mail = EmailMultiAlternatives(
        subject="Thank you for registering to our app!",
        body=content,
        from_email=settings.EMAIL_HOST_USER,
        to=[to_email],
    )
    mail.content_subtype = "html"
    mail.send()
