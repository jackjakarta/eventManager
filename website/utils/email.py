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


# Sends an email to self when contact form is filled
def send_contact_mail(name, message, reply_to):
    subject = f"New Contact Form Entry ({reply_to})"
    user_message = f"Reply To: {reply_to}\nName: {name}\n\n{message}"

    send_mail(
        subject=subject,
        message=user_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=["support@evntmngr.xyz"],
    )


# Sends an email to the user when contact form is filled
def send_contact_confirm_mail(name, email, message):
    context = {
        "name": name,
        "email": email,
        "message": message,
    }

    template = get_template("website/email/contact_confirm_email.html")
    content = template.render(context)

    mail = EmailMultiAlternatives(
        subject="We'll be in touch soon!",
        body=content,
        from_email=settings.EMAIL_HOST_USER,
        to=[email],
    )
    mail.content_subtype = "html"
    mail.send()
