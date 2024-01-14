from django.urls import path
from . import views


urlpatterns = [
    # Static Pages
    path('', views.home, name='home'),
    path('docs/', views.app_docs, name='docs'),  # Not implemented
    path('docs/api/', views.app_docs_api, name='docs_api'),

    # AI API Calls
    path('assistant/', views.ai_assistant_event, name='assistant'),
    path('assistant/flyer-generator/', views.ai_assistant_image, name='assistant_image'),

    # Venues, Promoters, Events
    path('venues/', views.venues, name='venues'),
    path('venues/<int:pk>/', views.venue_page, name='venue_page'),

    path('promoters/', views.promoters, name='promoters'),
    path('promoters/<int:pk>/', views.promoter_page, name='promoter_page'),

    path('events/', views.events, name='events'),
    path('events/<int:pk>/', views.event_page, name='event_page'),
    path('events/attend/<int:pk>/', views.event_attend, name='event_attend'),
    path('events/unattend/<int:pk>/', views.event_un_attend, name='event_unattend'),

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

    # User Pages
    path('user/<int:pk>/', views.user_profile, name='profile'),
    path('user/<int:pk>/promoters/', views.user_promoters, name='user_promoters'),
    path('user/<int:pk>/events/', views.user_events, name='user_events'),
    path('user/<int:pk>/venues/', views.user_venues, name='user_venues'),
    path('user/<int:pk>/events-attending/', views.user_events_attending, name='user_events_attending'),

    # User Authentication
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    # Utility Views
    path('send-test-email/', views.send_test_email, name='send_test_email'),
    path('send-newsletter/', views.send_newsletter_email, name='send_newsletter_email'),
    path('subscribe-newsletter/', views.subscribe_newsletter, name='subscribe_newsletter'),
]
