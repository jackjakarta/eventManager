from django.urls import path

from website.views.model import artists, events, promoters, venues
from website.views.model import artist_page, event_page, promoter_page, venue_page
from website.views.model import (
    artist_events,
    venue_events,
    event_attend,
    event_un_attend,
)
from website.views.model import events_search


app_name = "model_pages"

urlpatterns = [
    # Artists, Venues, Promoters, Events
    path("artists/", artists, name="artists"),
    path("artists/<int:pk>/", artist_page, name="artist_page"),
    path("artists/<int:pk>/events/", artist_events, name="artist_events"),
    path("venues/", venues, name="venues"),
    path("venues/<int:pk>/", venue_page, name="venue_page"),
    path("venues/<int:pk>/events/", venue_events, name="venue_events"),
    path("promoters/", promoters, name="promoters"),
    path("promoters/<int:pk>/", promoter_page, name="promoter_page"),
    path("events/", events, name="events"),
    path("events/<int:pk>/", event_page, name="event_page"),
    path("events/attend/<int:pk>/", event_attend, name="event_attend"),
    path("events/unattend/<int:pk>/", event_un_attend, name="event_unattend"),
    path("events/search/", events_search, name="events_search"),
]
