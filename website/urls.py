from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    # Web Pages
    path('', views.home, name='home'),
    path('venues/', views.venues, name='venues'),
    path('venues/<int:pk>/', views.venue_page, name='venue_page'),
    path('promoters/', views.promoters, name='promoters'),
    path('events/', views.events, name='events'),
    path('events/<int:pk>/', views.event_page, name='event_page'),

    # User Pages
    path('user/<int:pk>/', views.user_profile, name='profile'),
    path('user/<int:pk>/promoters/', views.user_promoters, name='user_promoters'),
    path('user/<int:pk>/events/', views.user_events, name='user_events'),
    path('user/<int:pk>/venues/', views.user_venues, name='user_venues'),

    # Add, Edit, Delete from DB forms
    path('edit-profile/<int:pk>/', views.edit_profile, name='edit_profile'),

    path('add-promoter/', views.add_promoter, name='add_promoter'),
    path('edit-promoter/<int:pk>/', views.edit_promoter, name='edit_promoter'),
    path('delete-promoter/<int:pk>/', views.delete_promoter, name='delete_promoter'),

    path('add-venue/', views.add_venue, name='add_venue'),
    path('edit-venue/<int:pk>/', views.edit_venue, name='edit_venue'),
    path('delete-venue/<int:pk>/', views.delete_venue, name='delete_venue'),

    path('add-event/', views.add_event, name='add_event'),
    path('edit-event/<int:pk>/', views.edit_event, name='edit_event'),
    path('delete-event/<int:pk>/', views.delete_event, name='delete_event'),

    # User Authentication
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
