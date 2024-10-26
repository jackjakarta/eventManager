from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from users.utils.decorators import user_is_authenticated
from website.forms import AddArtistForm, AddPromoterForm, AddVenueForm, AddEventForm
from website.models import Event, Artist, Venue, Promoter


# Add, Edit, Delete from DB forms
@user_is_authenticated
def add_artist(request):
    if request.method == "POST":
        form = AddArtistForm(request.POST, request.FILES, user=request.user)

        if form.is_valid() and form.check_for_moderation():
            form.save()
            messages.success(request, "You have successfully added an artist.")
            return redirect("website:user_profile:user_artists", pk=request.user.id)
        else:
            messages.error(
                request, "Your form is not valid or contains harmful language."
            )
            return render(
                request,
                "website/forms/add_artist.html",
                {
                    "form": form,
                },
            )
    else:
        form = AddArtistForm()
        return render(
            request,
            "website/forms/add_artist.html",
            {
                "form": form,
            },
        )


@user_is_authenticated
def edit_artist(request, pk):
    artist = get_object_or_404(Artist, id=pk)
    form = AddArtistForm(request.POST or None, request.FILES or None, instance=artist)

    if form.is_valid() and form.check_for_moderation():
        form.save()
        messages.success(request, "Artist updated successfully!")
        return redirect("website:model_pages:artist_page", pk=pk)

    return render(
        request,
        "website/forms/edit_artist.html",
        {
            "artist": artist,
            "form": form,
        },
    )


@user_is_authenticated
def delete_artist(request, pk):
    artist = get_object_or_404(Artist, id=pk)

    if request.user == artist.manager:
        artist.delete()
        messages.success(request, "Artist deleted successfully!")
        return redirect("website:user_profile:user_artists", pk=request.user.id)
    else:
        messages.error(request, "You can't delete this event!")
        return redirect("website:user_profile:user_profile", pk=request.user.id)


@user_is_authenticated
def add_promoter(request):
    if request.method == "POST":
        form = AddPromoterForm(request.POST, user=request.user)

        if form.is_valid() and form.check_for_moderation():
            form.save()
            messages.success(request, "You have successfully added a promoter.")
            return redirect("website:user_profile:user_promoters", pk=request.user.id)
        else:
            messages.error(
                request, "Your form is not valid or contains harmful language."
            )
            return render(
                request,
                "website/forms/add_promoter.html",
                {
                    "form": form,
                },
            )
    else:
        form = AddPromoterForm()
        return render(
            request,
            "website/forms/add_promoter.html",
            {
                "form": form,
            },
        )


@user_is_authenticated
def edit_promoter(request, pk):
    promoter = get_object_or_404(Promoter, id=pk)
    form = AddPromoterForm(request.POST or None, instance=promoter)

    if form.is_valid() and form.check_for_moderation():
        form.save()
        messages.success(request, "Promoter updated successfully!")
        return redirect("website:model_pages:promoter_page", pk=pk)

    return render(
        request,
        "website/forms/edit_promoter.html",
        {
            "promoter": promoter,
            "form": form,
        },
    )


@user_is_authenticated
def delete_promoter(request, pk):
    promoter = get_object_or_404(Promoter, id=pk)

    if request.user == promoter.manager:
        promoter.delete()
        messages.success(request, "Promoter deleted successfully!")
        return redirect("website:user_profile:user_promoters", pk=request.user.id)
    else:
        messages.error(request, "You can't delete this promoter!")
        return redirect("website:user_profile:user_profile", pk=request.user.id)


@user_is_authenticated
def add_venue(request):
    if request.method == "POST":
        form = AddVenueForm(request.POST, request.FILES, user=request.user)
        if form.is_valid() and form.check_for_moderation():
            form.save()
            messages.success(request, "You have successfully added a venue.")
            return redirect("website:user_profile:user_venues", pk=request.user.id)
        else:
            messages.error(
                request, "Your form is not valid or contains harmful language."
            )
            return render(
                request,
                "website/forms/add_venue.html",
                {
                    "form": form,
                },
            )
    else:
        form = AddVenueForm()
        return render(
            request,
            "website/forms/add_venue.html",
            {
                "form": form,
            },
        )


@user_is_authenticated
def edit_venue(request, pk):
    venues_qs = get_object_or_404(Venue, id=pk)
    form = AddVenueForm(request.POST or None, request.FILES or None, instance=venues_qs)

    if form.is_valid() and form.check_for_moderation():
        form.save()
        messages.success(request, "Updated successfully!")
        return redirect("website:model_pages:venue_page", pk=pk)

    return render(
        request,
        "website/forms/edit_venue.html",
        {
            "venue": venues_qs,
            "form": form,
        },
    )


@user_is_authenticated
def delete_venue(request, pk):
    venue = get_object_or_404(Venue, id=pk)

    if request.user == venue.manager:
        venue.delete()
        messages.success(request, "Venue deleted successfully!")
        return redirect("website:user_profile:user_venues", pk=request.user.id)
    else:
        messages.error(request, "You can't delete this venue!")
        return redirect("website:user_profile:user_profile", pk=request.user.id)


@user_is_authenticated
def add_event(request):
    if request.method == "POST":
        form = AddEventForm(request.POST, request.FILES, user=request.user)
        if form.is_valid() and form.check_for_moderation():
            form.save()
            messages.success(request, "You have successfully added an event.")
            return redirect("website:user_profile:user_events", pk=request.user.id)
        else:
            messages.error(
                request, "Your form is not valid or contains harmful language."
            )
            return render(
                request,
                "website/forms/add_event.html",
                {
                    "form": form,
                },
            )
    else:
        form = AddEventForm(user=request.user)
        return render(
            request,
            "website/forms/add_event.html",
            {
                "form": form,
            },
        )


@user_is_authenticated
def edit_event(request, pk):
    events_qs = get_object_or_404(Event, id=pk)
    form = AddEventForm(
        request.POST or None,
        request.FILES or None,
        instance=events_qs,
        user=request.user,
    )

    if form.is_valid() and form.check_for_moderation():
        form.save()
        messages.success(request, "Updated successfully!")
        return redirect("website:model_pages:event_page", pk=pk)

    return render(
        request,
        "website/forms/edit_event.html",
        {
            "event": events_qs,
            "form": form,
        },
    )


@user_is_authenticated
def delete_event(request, pk):
    event = get_object_or_404(Event, id=pk)

    if request.user == event.manager:
        event.delete()
        messages.success(request, "Event deleted successfully!")
        return redirect("website:user_profile:user_events", pk=request.user.id)
    else:
        messages.error(request, "You can't delete this event!")
        return redirect("website:user_profile:user_profile", pk=request.user.id)
