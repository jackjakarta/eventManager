from django.contrib import messages
from django.shortcuts import render, redirect

from website.models import Event, Artist, Promoter, Venue
from website.utils.email import send_contact_mail, send_contact_confirm_mail


# Static Pages Views
def home(request):
    events_qs = Event.objects.all().order_by("event_date")[:5]
    artists_qs = Artist.objects.all().order_by("updated_at")[:3]
    promoters_qs = Promoter.objects.all().order_by("updated_at")[:2]
    venues_qs = Venue.objects.all().order_by("updated_at")[:3]
    return render(request, "website/home.html", {
        "events": events_qs,
        "artists": artists_qs,
        "promoters": promoters_qs,
        "venues": venues_qs,
    })


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        send_contact_mail(
            name=name,
            message=message,
            reply_to=email
        )

        send_contact_confirm_mail(
            name=name,
            email=email,
            message=message
        )

        messages.success(request, f"Thank you, {name}. We'll get back to you as soon as possible!")
        return redirect("website:static_pages:home")
    else:
        return render(request, "website/contact.html", {})


def app_docs(request):
    return render(request, "404.html", {})


def app_docs_api(request):
    return render(request, "website/docs/docs_api.html", {})


def privacy_policy(request):
    return render(request, "website/docs/privacy_policy.html", {})
