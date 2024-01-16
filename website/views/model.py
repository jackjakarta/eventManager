from django.shortcuts import render, redirect
from django.contrib import messages

from website.forms import AddPromoterForm, AddVenueForm, AddEventForm
from website.models import Event, Venue, Promoter


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


def venue_events(request, pk):
    venue_name = Venue.objects.get(id=pk)
    events_at_venue = Event.objects.filter(venue_id=pk)
    return render(request, "website/venue_events.html", {
        "events": events_at_venue,
        "venue": venue_name,
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

        return redirect("website:model_pages:event_page", pk=pk)
    else:
        messages.error(request, "You have to be logged in to use this feature.")
        return redirect("website:user_auth:login")


def event_un_attend(request, pk):
    if request.user.is_authenticated:
        event = Event.objects.get(id=pk)

        if request.user in event.attendees.all():
            event.attendees.remove(request.user)
            messages.success(request, "You have unattended this event.")
        else:
            messages.error(request, "You were not attending this event.")

        return redirect("website:model_pages:event_page", pk=pk)
    else:
        messages.error(request, "You have to be logged in to use this feature.")
        return redirect("website:user_auth:login")


