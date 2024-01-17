from django.shortcuts import render
from website.models import Event


# Static Pages Views
def home(request):
    events_qs = Event.objects.all().order_by("event_date")[:5]
    return render(request, "website/home.html", {
        "events": events_qs,
    })


def app_docs(request):
    pass


def app_docs_api(request):
    return render(request, "website/docs_api.html", {})
