from django.shortcuts import render, redirect
from django.contrib import messages

from website.forms import AddPromoterForm, AddVenueForm, AddEventForm
from website.models import Event, Venue, Promoter


# Add, Edit, Delete from DB forms
def add_promoter(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddPromoterForm(request.POST, user=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "You have successfully added a promoter.")
                return redirect("website:user_profile:user_promoters", pk=request.user.id)
            else:
                messages.error(request, "Your form is not valid.")
                return render(request, "website/forms/add_promoter.html", {
                    "form": form,
                })
        else:
            form = AddPromoterForm()
            return render(request, "website/forms/add_promoter.html", {
                "form": form,
            })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("website:user_auth:login")


def edit_promoter(request, pk):
    if request.user.is_authenticated:
        promoter = Promoter.objects.get(id=pk)
        form = AddPromoterForm(request.POST or None, instance=promoter)
        if form.is_valid():
            form.save()
            messages.success(request, "Promoter updated successfully!")
            return redirect("website:model_pages:promoter_page", pk=pk)

        return render(request, "website/forms/edit_promoter.html", {
            "promoter": promoter,
            "form": form,
        })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("website:user_auth:login")


def delete_promoter(request, pk):
    if request.user.is_authenticated:
        promoter = Promoter.objects.get(id=pk)
        promoter.delete()
        messages.success(request, "Promoter deleted successfully!")
        return redirect("website:user_profile:user_promoters", pk=request.user.id)
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("website:user_auth:login")


def add_venue(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddVenueForm(request.POST, request.FILES, user=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "You have successfully added a venue.")
                return redirect("website:user_profile:user_venues", pk=request.user.id)
            else:
                messages.error(request, "Your form is not valid.")
                return render(request, "website/forms/add_venue.html", {
                    "form": form,
                })
        else:
            form = AddVenueForm()
            return render(request, "website/forms/add_venue.html", {
                "form": form,
            })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("website:user_auth:login")


def edit_venue(request, pk):
    if request.user.is_authenticated:
        venues_qs = Venue.objects.get(id=pk)
        form = AddVenueForm(request.POST or None, request.FILES or None, instance=venues_qs)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated successfully!")
            return redirect("website:model_pages:venue_page", pk=pk)

        return render(request, "website/forms/edit_venue.html", {
            "venue": venues_qs,
            "form": form,
        })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("website:user_auth:login")


def delete_venue(request, pk):
    if request.user.is_authenticated:
        venue = Venue.objects.get(id=pk)
        venue.delete()
        messages.success(request, "Venue deleted successfully!")
        return redirect("website:user_profile:user_venues", pk=request.user.id)
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("website:user_auth:login")


def add_event(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddEventForm(request.POST, request.FILES, user=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "You have successfully added an event.")
                return redirect("website:user_profile:user_events", pk=request.user.id)
            else:
                messages.error(request, "Your form is not valid.")
                return render(request, "website/forms/add_event.html", {
                    "form": form,
                })
        else:
            form = AddEventForm(user=request.user)
            return render(request, "website/forms/add_event.html", {
                "form": form,
            })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("website:user_auth:login")


def edit_event(request, pk):
    if request.user.is_authenticated:
        events_qs = Event.objects.get(id=pk)
        form = AddEventForm(request.POST or None, request.FILES or None, instance=events_qs, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated successfully!")
            return redirect("website:model_pages:event_page", pk=pk)

        return render(request, "website/forms/edit_event.html", {
            "event": events_qs,
            "form": form,
        })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("website:user_auth:login")


def delete_event(request, pk):
    if request.user.is_authenticated:
        event = Event.objects.get(id=pk)
        event.delete()
        messages.success(request, "Event deleted successfully!")
        return redirect("website:user_profile:user_events", pk=request.user.id)
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("website:user_auth:login")
