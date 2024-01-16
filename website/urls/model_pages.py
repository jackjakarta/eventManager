from django.urls import path

from website.views.model import venues, events, promoters
from website.views.model import venue_page, event_page, promoter_page
from website.views.model import venue_events, event_attend, event_un_attend


app_name = 'model_pages'

urlpatterns = [
    # Venues, Promoters, Events
    path('venues/', venues, name='venues'),
    path('venues/<int:pk>/', venue_page, name='venue_page'),
    path('venues/<int:pk>/events/', venue_events, name='venue_events'),

    path('promoters/', promoters, name='promoters'),
    path('promoters/<int:pk>/', promoter_page, name='promoter_page'),

    path('events/', events, name='events'),
    path('events/<int:pk>/', event_page, name='event_page'),
    path('events/attend/<int:pk>/', event_attend, name='event_attend'),
    path('events/unattend/<int:pk>/', event_un_attend, name='event_unattend'),
]
