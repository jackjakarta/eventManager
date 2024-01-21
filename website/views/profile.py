from django.shortcuts import render, redirect
from django.contrib import messages

from website.forms import EditProfileForm
from website.models import Profile, Event, Venue, Promoter, Artist


# User Views
def user_profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        events_user = Event.objects.filter(manager_id=pk).order_by('event_date')[:2]
        promoters_user = Promoter.objects.filter(manager_id=pk).order_by('updated_at')[:2]
        venues_user = Venue.objects.filter(manager_id=pk).order_by('updated_at')[:2]
        return render(request, "website/profile/user_profile.html", {
            "profile": profile,
            "events": events_user,
            "promoters": promoters_user,
            "venues": venues_user,
        })
    else:
        messages.error(request, "You are not logged in!")
        return redirect("website:user_auth:login")


def edit_profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        form = EditProfileForm(request.POST or None, request.FILES or None, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("website:user_profile:profile", pk=pk)

        return render(request, "website/profile/edit_profile.html", {
            "profile": profile,
            "form": form,
        })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("website:user_auth:login")


def user_artists(request, pk):
    if request.user.is_authenticated:
        artists_qs = Artist.objects.filter(manager_id=pk)
        return render(request, "website/profile/user_artists.html", {
            "artists": artists_qs,
        })
    else:
        messages.error(request, "You have to be logged in to see your events.")
        return redirect("website:user_auth:login")


def user_events(request, pk):
    if request.user.is_authenticated:
        events_qs = Event.objects.filter(manager_id=pk)
        return render(request, "website/profile/user_events.html", {
            "events": events_qs,
        })
    else:
        messages.error(request, "You have to be logged in to see your events.")
        return redirect("website:user_auth:login")


def user_promoters(request, pk):
    if request.user.is_authenticated:
        promoters_qs = Promoter.objects.filter(manager_id=pk)
        return render(request, "website/profile/user_promoters.html", {
            "promoters": promoters_qs,
        })
    else:
        messages.error(request, "You have to be logged in to see your promoters.")
        return redirect("website:user_auth:login")


def user_venues(request, pk):
    if request.user.is_authenticated:
        venues_qs = Venue.objects.filter(manager_id=pk)
        return render(request, "website/profile/user_venues.html", {
            "venues": venues_qs,
        })
    else:
        messages.error(request, "You have to be logged in to see your venues.")
        return redirect("website:user_auth:login")


def user_events_attending(request, pk):
    if request.user.is_authenticated:
        attending_events = Event.objects.filter(attendees=pk)
        return render(request, "website/profile/user_events_attending.html", {
            "events": attending_events,
        })
    else:
        messages.error(request, "You are not logged in.")
        return redirect("website:user_auth:login")
