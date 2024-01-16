from django.shortcuts import render


# Static Pages Views
def home(request):
    return render(request, "website/home.html", {})


def app_docs(request):
    pass


def app_docs_api(request):
    return render(request, "website/docs_api.html", {})
