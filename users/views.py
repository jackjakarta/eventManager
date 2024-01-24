from django.shortcuts import render, redirect, HttpResponse, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.utils import timezone
from django.utils.decorators import decorator_from_middleware

from .forms import PasswordForm
from .models import Activation, AVAILABILITY
from .middlewares.activation_middleware import ActivationMiddleware
from .utils.constants import ACTIVATION_AVAILABILITY


@decorator_from_middleware(ActivationMiddleware)
def activate_user(request, token):
    activation = get_object_or_404(Activation, token=token)
    user = activation.user

    if request.method == "GET":
        form = PasswordForm(user)
    else:
        form = PasswordForm(user, request.POST)
        if form.is_valid():
            form.save()

            user.is_active = True
            user.save()

            activation.activated_at = timezone.now()
            activation.save()

            messages.success(request, "Your account has been activated. You can log in into your account.")
            return redirect("website:user_auth:login")

    return render(request, "users/set_password.html", {
        "form": form,
        "token": token,
    })


@decorator_from_middleware(ActivationMiddleware)
def reset_token(request, token):
    if request.method == "GET":
        return render(request, "users/reset_token.html", {
            "token": token,
        })

    activation = get_object_or_404(Activation, token=token)
    activation.expires_at = timezone.now() + timezone.timedelta(**AVAILABILITY)
    activation.save()
    send_activation_email(activation.user)

    return HttpResponse('Token has been reset,'
                        'Please follow the instructions received on your email')


def send_activation_email(user):
    domain = Site.objects.get_current().domain
    url = reverse("activate", args=(user.activation.token, ))
    activation_url = f"{domain}{url}"
    print(activation_url)

    context = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "activation_url": activation_url,
        "availability": ACTIVATION_AVAILABILITY,
    }

    template = get_template("users/email/activation_email.html")
    content = template.render(context)
    mail = EmailMultiAlternatives(
        subject="Your account has been created.",
        body=content,
        from_email="no-reply@evntmngr.xyz",
        to=[user.email]
    )

    mail.content_subtype = "html"
    mail.send()


# CHECK WITH PIZZA CODE
