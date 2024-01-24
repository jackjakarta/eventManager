from django.urls import path
from .views import activate_user, reset_token


urlpatterns = [
    path('activate/<str:token>/', activate_user, name='activate'),
    path('reset-token/<str:token>/', reset_token, name='reset_token'),
]
