from django.urls import path, include

app_name = "website"  # Keep this consistent with your app's name


urlpatterns = [
    path("", include("website.urls.static_pages")),
    path("", include("website.urls.model_pages")),
    path("", include("website.urls.api_calls")),
    path("", include("website.urls.update_db")),
    path("", include("website.urls.user_auth")),
    path("", include("website.urls.user_profile")),
    path("", include("website.urls.utility")),
]
