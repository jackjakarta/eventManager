from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives


# Email Functions
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
