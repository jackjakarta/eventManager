from django.urls import path

from website.views.update import add_artist, edit_artist, delete_artist
from website.views.update import add_event, edit_event, delete_event
from website.views.update import add_promoter, edit_promoter, delete_promoter
from website.views.update import add_venue, edit_venue, delete_venue

app_name = 'update_db'

urlpatterns = [
    # Add, Edit, Delete from DB forms
    path('add-artist/', add_artist, name='add_artist'),
    path('edit-artist/<int:pk>/', edit_artist, name='edit_artist'),
    path('delete-artist/<int:pk>/', delete_artist, name='delete_artist'),

    path('add-promoter/', add_promoter, name='add_promoter'),
    path('edit-promoter/<int:pk>/', edit_promoter, name='edit_promoter'),
    path('delete-promoter/<int:pk>/', delete_promoter, name='delete_promoter'),

    path('add-venue/', add_venue, name='add_venue'),
    path('edit-venue/<int:pk>/', edit_venue, name='edit_venue'),
    path('delete-venue/<int:pk>/', delete_venue, name='delete_venue'),

    path('add-event/', add_event, name='add_event'),
    path('edit-event/<int:pk>/', edit_event, name='edit_event'),
    path('delete-event/<int:pk>/', delete_event, name='delete_event'),
]
