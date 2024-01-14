import time
import pytz

from decouple import config
from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Profile, Event, Venue, Promoter, APIKey
from .serializers import EventSerializer, VenueSerializer, PromoterSerializer
from .forms import SignUpForm, AddPromoterForm, AddVenueForm, AddEventForm, EditProfileForm  # Model Forms
from .forms import GPTAssistantsApiForm, DallEImageForm
from .utils import send_register_user_email, generate_api_key
from .ai import GPTAssistantsApi, ImageDallE

OPENAI_ASSISTANT_ID = config("OPENAI_ASSISTANT_ID")


# Static Pages Views
def home(request):
    return render(request, "website/home.html", {})


def app_docs(request):
    pass


def app_docs_api(request):
    return render(request, "website/docs_api.html", {})


# AI API Call Views
def ai_assistant_event(request):
    if request.user.is_authenticated:
        ai = GPTAssistantsApi(OPENAI_ASSISTANT_ID)

        if request.method == "POST":
            form = GPTAssistantsApiForm(request.POST)

            if form.is_valid():
                prompt = form.cleaned_data["prompt"]
                # custom_instructions = form.cleaned_data["custom_instructions"]

                ai.create_thread()
                ai.create_message(prompt)
                ai.create_run()

                while True:
                    ai.retrieve_run()

                    if ai.run.status == "completed":
                        ai.list_messages()

                        m_list = [x.content[0].text.value for x in reversed(ai.messages.data)]
                        user_prompt = m_list[0]
                        event_info = m_list[1]

                        # Split the string to extract Event Name, Event Flyer, and Event Description
                        event_name_start = event_info.find('Event Name: ')
                        event_flyer_start = event_info.find('Event Flyer: ')
                        event_description_start = event_info.find('Event Description: ')

                        event_name = event_info[event_name_start + len('Event Name: '):event_flyer_start].strip()
                        event_flyer = event_info[
                                      event_flyer_start + len('Event Flyer: '):event_description_start].strip()
                        event_description = event_info[event_description_start + len('Event Description: '):].strip()

                        return render(request, "website/ai_page.html", {
                            "user_prompt": user_prompt,
                            "event_name": event_name,
                            "event_flyer": event_flyer,
                            "event_description": event_description,
                        })
                    elif ai.run.status == "failed":
                        messages.error(request, "Something went wrong. Please try again...")
                        return redirect("assistant")
                    else:
                        time.sleep(3)
                        continue
        else:
            form = GPTAssistantsApiForm()
            return render(request, "website/ai_page.html", {
                "form": form,
            })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("login")


def ai_assistant_image(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = DallEImageForm(request.POST)
            if form.is_valid():
                user_prompt = form.cleaned_data["image_prompt"]
                prompt_for_model = (f"Generate an event flyer based on this description:\n\n{user_prompt}.\n\n"
                                    f"Follow the description precisely.")

                img_ai = ImageDallE()
                img_ai.generate_image(prompt_for_model)
                img_url = img_ai.image_url

                return render(request, "website/ai_image_page.html", {
                    "image": img_url,
                })
        else:
            form = DallEImageForm()
            return render(request, "website/ai_image_page.html", {
                "form": form,
            })


# Events, Venues and Promoters Views
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
    promoters_qs = Promoter.objects.all()
    return render(request, "website/promoters.html", {
        "promoters": promoters_qs,
    })


def promoter_page(request, pk):
    promoter = Promoter.objects.get(id=pk)
    return render(request, "website/promoter_page.html", {
        "promoter": promoter,
    })


def events(request):
    events_qs = Event.objects.all().order_by("-event_date")
    return render(request, "website/events.html", {
        "events": events_qs,
    })


def event_page(request, pk):
    event = Event.objects.get(id=pk)
    return render(request, "website/event_page.html", {
        "event": event,
    })


def event_attend(request, pk):
    if request.user.is_authenticated:
        event = Event.objects.get(id=pk)

        if request.user not in event.attendees.all():
            event.attendees.add(request.user)
            messages.success(request, "You are attending this event!")
        else:
            messages.error(request, "You are already attending this event!")

        return redirect("event_page", pk=pk)
    else:
        messages.error(request, "You have to be logged in to use this feature.")
        return redirect("login")


def event_un_attend(request, pk):
    if request.user.is_authenticated:
        event = Event.objects.get(id=pk)

        if request.user in event.attendees.all():
            event.attendees.remove(request.user)
            messages.success(request, "You have unattended this event.")
        else:
            messages.error(request, "You were not attending this event.")

        return redirect("event_page", pk=pk)
    else:
        messages.error(request, "You have to be logged in to use this feature.")
        return redirect("login")


# Add, Edit, Delete from DB forms
def add_promoter(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddPromoterForm(request.POST, user=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "You have successfully added a promoter.")
                return redirect("user_promoters", pk=request.user.id)
            else:
                messages.error(request, "Your form is not valid.")
                return render(request, "website/add_promoter.html", {
                    "form": form,
                })
        else:
            form = AddPromoterForm()
            return render(request, "website/add_promoter.html", {
                "form": form,
            })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("login")


def edit_promoter(request, pk):
    if request.user.is_authenticated:
        promoter = Promoter.objects.get(id=pk)
        form = AddPromoterForm(request.POST or None, instance=promoter)
        if form.is_valid():
            form.save()
            messages.success(request, "Promoter updated successfully!")
            return redirect("promoter_page", pk=pk)

        return render(request, "website/edit_promoter.html", {
            "promoter": promoter,
            "form": form,
        })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("login")


def delete_promoter(request, pk):
    if request.user.is_authenticated:
        promoter = Promoter.objects.get(id=pk)
        promoter.delete()
        messages.success(request, "Promoter deleted successfully!")
        return redirect("user_promoters", pk=request.user.id)
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("login")


def add_venue(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddVenueForm(request.POST, request.FILES, user=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "You have successfully added a venue.")
                return redirect("user_venues", pk=request.user.id)
            else:
                messages.error(request, "Your form is not valid.")
                return render(request, "website/add_venue.html", {
                    "form": form,
                })
        else:
            form = AddVenueForm()
            return render(request, "website/add_venue.html", {
                "form": form,
            })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("login")


def edit_venue(request, pk):
    if request.user.is_authenticated:
        venues_qs = Venue.objects.get(id=pk)
        form = AddVenueForm(request.POST or None, request.FILES or None, instance=venues_qs)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated successfully!")
            return redirect("venue_page", pk=pk)

        return render(request, "website/edit_venue.html", {
            "venue": venues_qs,
            "form": form,
        })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("login")


def delete_venue(request, pk):
    if request.user.is_authenticated:
        venue = Venue.objects.get(id=pk)
        venue.delete()
        messages.success(request, "Venue deleted successfully!")
        return redirect("user_venues", pk=request.user.id)
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("login")


def add_event(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddEventForm(request.POST, request.FILES, user=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "You have successfully added an event.")
                return redirect("user_events", pk=request.user.id)
            else:
                messages.error(request, "Your form is not valid.")
                return render(request, "website/add_event.html", {
                    "form": form,
                })
        else:
            form = AddEventForm(user=request.user)
            return render(request, "website/add_event.html", {
                "form": form,
            })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("login")


def edit_event(request, pk):
    if request.user.is_authenticated:
        events_qs = Event.objects.get(id=pk)
        form = AddEventForm(request.POST or None, request.FILES or None, instance=events_qs, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated successfully!")
            return redirect("event_page", pk=pk)

        return render(request, "website/edit_event.html", {
            "event": events_qs,
            "form": form,
        })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("login")


def delete_event(request, pk):
    if request.user.is_authenticated:
        event = Event.objects.get(id=pk)
        event.delete()
        messages.success(request, "Event deleted successfully!")
        return redirect("user_events", pk=request.user.id)
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("login")


def edit_profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        form = EditProfileForm(request.POST or None, request.FILES or None, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile", pk=pk)

        return render(request, "website/edit_profile.html", {
            "profile": profile,
            "form": form,
        })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("login")


# User Views
def user_profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        events_user = Event.objects.filter(manager_id=pk).order_by('event_date')[:2]
        promoters_user = Promoter.objects.filter(manager_id=pk).order_by('updated_at')[:2]
        venues_user = Venue.objects.filter(manager_id=pk).order_by('updated_at')[:2]
        api_key = APIKey.objects.get(user_id=pk)
        return render(request, "website/user_profile.html", {
            "profile": profile,
            "events": events_user,
            "promoters": promoters_user,
            "venues": venues_user,
            "key": api_key,
        })
    else:
        messages.error(request, "You are not logged in!")
        return redirect("login")


def user_events(request, pk):
    if request.user.is_authenticated:
        events_user = Event.objects.filter(manager_id=pk)
        return render(request, "website/user_events.html", {
            "user_events": events_user,
        })
    else:
        messages.error(request, "You have to be logged in to see your events.")
        return redirect("login")


def user_promoters(request, pk):
    if request.user.is_authenticated:
        promoters_qs = Promoter.objects.filter(manager_id=pk)
        return render(request, "website/user_promoters.html", {
            "promoters": promoters_qs,
        })
    else:
        messages.error(request, "You have to be logged in to see your promoters.")
        return redirect("login")


def user_venues(request, pk):
    if request.user.is_authenticated:
        venues_qs = Venue.objects.filter(manager_id=pk)
        return render(request, "website/user_venues.html", {
            "venues": venues_qs,
        })
    else:
        messages.error(request, "You have to be logged in to see your venues.")
        return redirect("login")


def user_events_attending(request, pk):
    if request.user.is_authenticated:
        attending_events = Event.objects.filter(attendees=pk)
        return render(request, "website/user_events_attending.html", {
            "events": attending_events,
        })
    else:
        messages.error(request, "You are not logged in.")
        return redirect("login")


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
                    send_register_user_email(user.first_name, user.email)  # Change function after test
                    print("Email sent to user!")
                else:
                    print("User logged in 1 day ago.")

                # Login and redirect
                login(request, user)
                messages.success(request, "You have logged in.")
                return redirect("profile", pk=user.id)
            else:
                messages.error(request, "There was a problem logging you in.")
                return redirect("login")
        else:
            return render(request, "website/login.html", {})
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
                user = form.save()

                # Generate and assign API Key to user
                api_key = generate_api_key()
                APIKey.objects.create(user=user, api_key=api_key)

                # Get user data from form
                # first_name = form.cleaned_data["first_name"]
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password1"]

                # Login user
                user = authenticate(request, email=email, password=password)
                login(request, user)

                # Send welcome email to user
                # send_register_user_email(first_name, email)

                messages.success(request, "You have successfully registered and have been logged in.")
                return redirect("profile", pk=user.id)
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


def send_newsletter_email(request):
    pass


def send_test_email(request):
    first_name = "Alex"
    email_address = "alex.termure@yahoo.com"
    send_register_user_email(first_name, email_address)

    messages.success(request, "Email sent!")
    return redirect("home")


# API View Sets
class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class VenuesViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class PromotersViewSet(viewsets.ModelViewSet):
    queryset = Promoter.objects.all()
    serializer_class = PromoterSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
