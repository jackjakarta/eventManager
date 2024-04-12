from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

from website.models import Event, Venue, Promoter, Artist
from users.utils.decorators import user_is_authenticated


# Events, Artists, Venues and Promoters Views
def artists(request):
    artists_qs = Artist.objects.all()
    return render(request, "website/artists/artists.html", {
        "artists": artists_qs,
    })


def artist_page(request, pk):
    artist_qs = Artist.objects.get(id=pk)
    paginator = Paginator(artist_qs, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "website/artists/artist_page.html", {
        "page_obj": page_obj,
    })


def artist_events(request, pk):
    artist_name = Artist.objects.get(id=pk)
    events_with_artist = Event.objects.filter(artists=pk)
    return render(request, "website/artists/artist_events.html", {
        "artist": artist_name,
        "events": events_with_artist,
    })


def venues(request):
    venues_qs = Venue.objects.all().order_by("-updated_at")
    paginator = Paginator(venues_qs, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "website/venues/venues.html", {
        "page_obj": page_obj,
    })


def venue_page(request, pk):
    venue = Venue.objects.get(id=pk)
    return render(request, "website/venues/venue_page.html", {
        "venue": venue,
    })


def venue_events(request, pk):
    venue_name = Venue.objects.get(id=pk)
    events_at_venue = Event.objects.filter(venue_id=pk)
    return render(request, "website/venues/venue_events.html", {
        "events": events_at_venue,
        "venue": venue_name,
    })


def promoters(request):
    promoters_qs = Promoter.objects.all().order_by("-updated_at")
    paginator = Paginator(promoters_qs, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "website/promoters/promoters.html", {
        "page_obj": page_obj,
    })


def promoter_page(request, pk):
    promoter = Promoter.objects.get(id=pk)
    return render(request, "website/promoters/promoter_page.html", {
        "promoter": promoter,
    })


def events(request):
    events_qs = Event.objects.all().order_by("-event_date")
    paginator = Paginator(events_qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "website/events/events.html", {
        "page_obj": page_obj,
    })


def event_page(request, pk):
    event = Event.objects.get(id=pk)
    return render(request, "website/events/event_page.html", {
        "event": event,
    })


@user_is_authenticated
def event_attend(request, pk):
    event = get_object_or_404(Event, id=pk)

    if request.user not in event.attendees.all():
        event.attendees.add(request.user)
        messages.success(request, "You are attending this event!")
    else:
        messages.error(request, "You are already attending this event!")

    return redirect("website:model_pages:event_page", pk=pk)


@user_is_authenticated
def event_un_attend(request, pk):
    event = get_object_or_404(Event, id=pk)

    if request.user in event.attendees.all():
        event.attendees.remove(request.user)
        messages.success(request, "You have unattended this event.")
    else:
        messages.error(request, "You were not attending this event.")

    return redirect("website:model_pages:event_page", pk=pk)


def events_search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        events_qs = Event.objects.filter(name__contains=searched.title())
        paginator = Paginator(events_qs, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, "website/events/events_search.html", {
            "searched": searched,
            "page_obj": page_obj,
        })
