from django.urls import path, include

from website.views.auth import login_user, logout_user, register_user, generate_api_key

app_name = "user_auth"

urlpatterns = [
    # User Authentication
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("register/", register_user, name="register"),
    path("social-auth/", include("social_django.urls")),
    path("generate-api-key/", generate_api_key, name="generate_api_key"),
]
