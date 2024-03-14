from django.urls import path, include
from rest_framework import routers

from .viewsets.social import get_posts, get_post_comments
from .viewsets.website import ArtistsViewSet, EventsViewSet, VenuesViewSet, PromotersViewSet
from .viewsets.website import get_newsletter_subs

app_name = 'api'


router = routers.DefaultRouter()

# Events, Venues, Artists, Promoters API Routes
router.register(r'artists', ArtistsViewSet, 'artists')
router.register(r'events', EventsViewSet, 'events')
router.register(r'venues', VenuesViewSet, 'venues')
router.register(r'promoters', PromotersViewSet, 'promoters')


urlpatterns = [
    path('', include(router.urls)),
    path('newsletter-list/', get_newsletter_subs, name='get_newsletter_list'),

    # Social App API Views
    path('posts/', get_posts, name='posts'),
    path('post-comments/<int:post_id>/', get_post_comments, name='post_comments'),
]
