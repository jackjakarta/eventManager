from django.urls import path
from website.views.auth import login_user, logout_user, register_user, generate_api_key


app_name = 'user_auth'

urlpatterns = [
    # User Authentication
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('generate-api-key/', generate_api_key, name='generate_api_key'),
]
