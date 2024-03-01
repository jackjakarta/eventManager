from django.shortcuts import render
from website.models import Event


# Static Pages Views
def home(request):
    events_qs = Event.objects.all().order_by("event_date")[:5]
    return render(request, "website/home.html", {
        "events": events_qs,
    })


def app_docs(request):
    return render(request, "404.html", {})


def app_docs_api(request):
    return render(request, "website/docs/docs_api.html", {})


def privacy_policy(request):
    return render(request, "website/docs/privacy_policy.html", {})
