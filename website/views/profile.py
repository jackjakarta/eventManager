from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from users.utils.decorators import user_is_authenticated
from website.forms import EditProfileForm, NewsletterCheckBoxForm
from website.models import Profile, Event, Venue, Promoter, Artist, UserGeneratedImage


# User Views
@user_is_authenticated
def user_profile(request, pk):
    profile = get_object_or_404(Profile, user_id=pk)

    events_user = Event.objects.filter(manager_id=pk).order_by('event_date')[:2]
    promoters_user = Promoter.objects.filter(manager_id=pk).order_by('updated_at')[:2]
    venues_user = Venue.objects.filter(manager_id=pk).order_by('updated_at')[:2]
    artists_user = Artist.objects.filter(manager_id=pk).order_by('updated_at')[:2]

    return render(request, "website/profile/user_profile.html", {
        "profile": profile,
        "events": events_user,
        "promoters": promoters_user,
        "venues": venues_user,
        "artists": artists_user,
    })


@user_is_authenticated
def edit_profile(request, pk):
    profile = get_object_or_404(Profile, user_id=pk)

    if request.user == profile.user:
        form = EditProfileForm(request.POST or None, request.FILES or None, instance=profile)
        newsletter_check = NewsletterCheckBoxForm(request.POST or None, instance=request.user)

        if form.is_valid() and newsletter_check.is_valid():
            form.save()
            newsletter_check.save()
            messages.success(request, "You have successfully edited your profile.")
            return redirect("website:user_profile:profile", pk=pk)

        return render(request, "website/profile/edit_profile.html", {
            "profile": profile,
            "form": form,
            "checkbox": newsletter_check,
        })
    else:
        messages.error(request, "You are not authorized to view this page.")
        return redirect("website:static_pages:home")


@user_is_authenticated
def user_artists(request, pk):
    if request.user.id == pk:
        artists_qs = Artist.objects.filter(manager_id=pk)
        return render(request, "website/profile/user_artists.html", {
            "artists": artists_qs,
        })
    else:
        messages.error(request, "You are not authorized to view this page.")
        return redirect("website:static_pages:home")


@user_is_authenticated
def user_events(request, pk):
    if request.user.id == pk:
        events_qs = Event.objects.filter(manager_id=pk)
        return render(request, "website/profile/user_events.html", {
            "events": events_qs,
        })
    else:
        messages.error(request, "You are not authorized to view this page.")
        return redirect("website:static_pages:home")


@user_is_authenticated
def user_promoters(request, pk):
    if request.user.id == pk:
        promoters_qs = Promoter.objects.filter(manager_id=pk)
        return render(request, "website/profile/user_promoters.html", {
            "promoters": promoters_qs,
        })
    else:
        messages.error(request, "You are not authorized to view this page.")
        return redirect("website:static_pages:home")


@user_is_authenticated
def user_venues(request, pk):
    if request.user.id == pk:
        venues_qs = Venue.objects.filter(manager_id=pk)
        return render(request, "website/profile/user_venues.html", {
            "venues": venues_qs,
        })
    else:
        messages.error(request, "You are not authorized to view this page.")
        return redirect("website:static_pages:home")


@user_is_authenticated
def user_events_attending(request, pk):
    if request.user.id == pk:
        attending_events = Event.objects.filter(attendees=pk)
        return render(request, "website/profile/user_events_attending.html", {
            "events": attending_events,
        })
    else:
        messages.error(request, "You are not authorized to view this page.")
        return redirect("website:static_pages:home")


@user_is_authenticated
def user_generated_images(request, pk):
    if request.user.id == pk:
        user_images = UserGeneratedImage.objects.filter(manager_id=pk)
        return render(request, "website/profile/user_event_flyers.html", {
            "user_images": user_images,
        })
    else:
        messages.error(request, "You are not authorized to view this page.")
        return redirect("website:static_pages:home")
