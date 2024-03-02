from django.shortcuts import render, redirect
from django.contrib import messages
from website.models import Event
from website.utils.email import send_contact_mail


# Static Pages Views
def home(request):
    events_qs = Event.objects.all().order_by("event_date")[:5]
    return render(request, "website/home.html", {
        "events": events_qs,
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
