from django.conf import settings
from django.core.mail import EmailMultiAlternatives, send_mail
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


# Sends an email to self when contact form is filled
def send_contact_mail(name, message, reply_to):
    subject = f"New Contact Form Entry ({reply_to})"
    email_from = settings.EMAIL_HOST_USER
    user_message = f"Reply To: {reply_to}\nName: {name}\n\n{message}"
    send_mail(subject=subject, message=user_message, from_email=email_from, recipient_list=["al.termure@gmail.com"])
