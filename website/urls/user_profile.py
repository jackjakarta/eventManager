from django.urls import path

from website.views import user_profile, edit_profile
from website.views import user_events, user_promoters, user_venues, user_events_attending


app_name = 'user_profile'

urlpatterns = [
    # User Pages
    path('edit-profile/<int:pk>/', edit_profile, name='edit_profile'),
    path('user/<int:pk>/', user_profile, name='profile'),
    path('user/<int:pk>/promoters/', user_promoters, name='user_promoters'),
    path('user/<int:pk>/events/', user_events, name='user_events'),
    path('user/<int:pk>/venues/', user_venues, name='user_venues'),
    path('user/<int:pk>/events-attending/', user_events_attending, name='user_events_attending'),
]
