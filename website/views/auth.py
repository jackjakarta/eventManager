from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from website.forms import SignUpForm


# Authentication Views
def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]

            # Authenticate
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You have logged in.")
                return redirect("website:user_profile:profile", pk=user.id)
            else:
                messages.error(request, "There was a problem logging you in.")
                return redirect("website:user_auth:login")
        else:
            return render(request, "website/auth/login.html", {})
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

                messages.success(request, "You have successfully registered. Check your email to activate "
                                          "your account.")
                return redirect("website:static_pages:home")
            else:
                messages.error(request, "Your form is not valid.")
                return redirect("website:user_auth:register")
        else:
            form = SignUpForm()
            return render(request, "website/auth/register.html", {
                "form": form
            })
    else:
        messages.error(request, "You are already registered.")
        return redirect("website:static_pages:home")
