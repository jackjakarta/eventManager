from django.contrib import messages
from django.shortcuts import redirect

from website.models import NewsletterSub
from website.utils.email import send_register_newsletter_email


# Utility Views
def subscribe_newsletter(request):
    if request.method == "POST":
        email = request.POST["email"]

        if email is not None:
            if not NewsletterSub.objects.filter(email=email).exists():
                NewsletterSub.objects.create(email=email)
                messages.success(request, "Thank you for subscribing to our Newsletter.")
                send_register_newsletter_email(email)
            else:
                messages.error(request, "You are already subscribed to the newsletter.")
        else:
            messages.error(request, "Something went wrong, please try again...")

        return redirect("website:static_pages:home")


def send_newsletter_email(request):
    pass


def send_test_email(request):
    email_address = "alex.termure@yahoo.com"
    send_register_newsletter_email(email_address)

    messages.success(request, "Email sent!")
    return redirect("website:static_pages:home")
