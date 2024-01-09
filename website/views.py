from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model

from .models import Profile, Event, Venue, Promoter
from .forms import SignUpForm, AddPromoterForm, AddVenueForm, AddEventForm
from .utils import send_register_user_email

AuthUser = get_user_model()


# Website Pages Views
def home(request):
    return render(request, "website/home.html", {})


def venues(request):
    venues_qs = Venue.objects.all()
    return render(request, "website/venues.html", {
        "venues": venues_qs,
    })


def venue_page(request, pk):
    venue = Venue.objects.get(id=pk)
    return render(request, "website/venue_page.html", {
        "venue": venue,
    })


def promoters(request):
    pass


def promoter_page(request, pk):
    promoter = Promoter.objects.get(id=pk)
    return render(request, "website/promoter_page.html", {
        "promoter": promoter,
    })


def events(request):
    events_qs = Event.objects.all().order_by('event_date')
    return render(request, "website/events.html", {
        "events": events_qs,
    })


def event_page(request, pk):
    event = Event.objects.get(id=pk)
    return render(request, "website/event_page.html", {
        "event": event,
    })


# Add, Edit, Delete from DB forms
def add_promoter(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddPromoterForm(request.POST, user=request.user)
            if form.is_valid():
                form.save()
                return redirect("home")
        else:
            form = AddPromoterForm()
            return render(request, "website/add_promoter.html", {
                "form": form,
            })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("home")


def edit_promoter(request, pk):
    if request.user.is_authenticated:
        promoter = Promoter.objects.get(id=pk)
        form = AddPromoterForm(request.POST or None, instance=promoter)
        if form.is_valid():
            form.save()
            messages.success(request, "Venue updated successfully!")
            return redirect("home")

        return render(request, "website/edit_promoter.html", {
            "promoter": promoter,
            "form": form,
        })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("home")


def delete_promoter(request, pk):
    if request.user.is_authenticated:
        promoter = Promoter.objects.get(id=pk)
        promoter.delete()
        messages.success(request, "Promoter deleted successfully!")
        return redirect("home")
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("home")


def add_venue(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddVenueForm(request.POST, request.FILES, user=request.user)
            if form.is_valid():
                form.save()
                return redirect("home")
        else:
            form = AddVenueForm()
            return render(request, "website/add_venue.html", {
                "form": form,
            })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("home")


def edit_venue(request, pk):
    if request.user.is_authenticated:
        venues_qs = Venue.objects.get(id=pk)
        form = AddVenueForm(request.POST or None, instance=venues_qs)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated successfully!")
            return redirect("venues")

        return render(request, "website/edit_venue.html", {
            "venues": venues_qs,
            "form": form,
        })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("home")


def delete_venue(request, pk):
    if request.user.is_authenticated:
        venue = Venue.objects.get(id=pk)
        venue.delete()
        messages.success(request, "Venue deleted successfully!")
        return redirect("venues")
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("home")


def add_event(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddEventForm(request.POST, user=request.user)
            if form.is_valid():
                form.save()
                return redirect("events")
        else:
            form = AddEventForm()
            return render(request, "website/add_event.html", {
                "form": form,
            })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("home")


def edit_event(request, pk):
    if request.user.is_authenticated:
        events_qs = Event.objects.get(id=pk)
        form = AddEventForm(request.POST or None, instance=events_qs)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated successfully!")
            return redirect("events")

        return render(request, "website/edit_event.html", {
            "events": events_qs,
            "form": form,
        })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("home")


def delete_event(request, pk):
    if request.user.is_authenticated:
        event = Event.objects.get(id=pk)
        event.delete()
        messages.success(request, "Event deleted successfully!")
        return redirect("events")
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("home")


# User Views
def user_profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        events_user = Event.objects.filter(manager_id=pk).order_by('event_date')[:5]
        promoters_user = Promoter.objects.filter(manager_id=pk).order_by('updated_at')[:5]
        venues_user = Venue.objects.filter(manager_id=pk).order_by('updated_at')[:5]
        return render(request, "website/user_profile.html", {
            "profile": profile,
            "events": events_user,
            "promoters": promoters_user,
            "venues": venues_user,
        })
    else:
        messages.error(request, "You are not logged in!")
        return redirect("home")


def user_events(request, pk):
    events_user = Event.objects.filter(manager_id=pk)
    return render(request, "website/user_events.html", {
        "user_events": events_user,
    })


def user_promoters(request, pk):
    promoters_qs = Promoter.objects.filter(manager_id=pk)
    return render(request, "website/user_promoters.html", {
        "promoters": promoters_qs,
    })


def user_venues(request, pk):
    venues_qs = Venue.objects.filter(manager_id=pk)
    return render(request, "website/user_venues.html", {
        "venues": venues_qs,
    })


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
                messages.success(request, "You've been logged in.")
                return redirect("home")
            else:
                messages.error(request, "There was a problem logging you in.")
        else:
            return render(request, "website/login.html")
    else:
        messages.error(request, "You are already logged in.")
        return redirect("home")


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")


def register_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()

                first_name = form.cleaned_data["first_name"]
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password1"]

                # Login User
                user = authenticate(request, email=email, password=password)
                login(request, user)

                messages.success(request, "You have successfully registered and have been logged in.")
                send_register_user_email(first_name, email)
                return redirect("home")
        else:
            form = SignUpForm()
            return render(request, "website/register.html", {
                "form": form
            })
    else:
        messages.error(request, "You are already registered.")
        return redirect("home")


# Utility Views
def not_found(request):
    response = render(request, "website/404.html")

    if not settings.DEBUG:
        if response.status_code == 404:
            return response
