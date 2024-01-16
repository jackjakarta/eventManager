import pytz
from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from website.forms import SignUpForm
from website.utils import send_register_user_email, send_login_user_email


# Authentication Views
def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]

            # Authenticate
            user = authenticate(request, email=email, password=password)

            if user is not None:
                # Check if user hasn't logged in a while.
                days_ago = datetime.now(pytz.utc) - timedelta(days=2)
                if user.last_login < days_ago:
                    send_login_user_email(user.first_name, user.email)  # Change function after test
                    print("Email sent to user!")
                else:
                    print("User logged in 1 day ago.")

                # Login and redirect
                login(request, user)
                messages.success(request, "You have logged in.")
                return redirect("website:user_profile:profile", pk=user.id)
            else:
                messages.error(request, "There was a problem logging you in.")
                return redirect("website:user_auth:login")
        else:
            return render(request, "website/login.html", {})
    else:
        messages.error(request, "You are already logged in.")
        return redirect("website:static_pages:home")


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("website:static_pages:home")


def register_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()

                # Get user data from form
                first_name = form.cleaned_data["first_name"]
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password1"]

                # Login user
                user = authenticate(request, email=email, password=password)
                login(request, user)

                # Send welcome email to user
                send_register_user_email(first_name, email)

                messages.success(request, "You have successfully registered and have been logged in.")
                return redirect("website:user_profile:profile", pk=user.id)
            else:
                messages.error(request, "Your form is not valid.")
                return redirect("website:user_auth:register")
        else:
            form = SignUpForm()
            return render(request, "website/register.html", {
                "form": form
            })
    else:
        messages.error(request, "You are already registered.")
        return redirect("website:static_pages:home")
