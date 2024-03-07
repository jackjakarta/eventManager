from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from .viewsets.social import PostsViewSet, PostCommentsViewSet
from .viewsets.website import ArtistsViewSet, EventsViewSet, VenuesViewSet, PromotersViewSet, get_newsletter_subs

router = routers.DefaultRouter()

# Events, Venues, Artists, Promoters API Routes
router.register(r'artists', ArtistsViewSet, 'artists')
router.register(r'events', EventsViewSet, 'events')
router.register(r'venues', VenuesViewSet, 'venues')
router.register(r'promoters', PromotersViewSet, 'promoters')

# Social App API Routes
router.register(r'posts', PostsViewSet, 'posts')
router.register(r'post-comments', PostCommentsViewSet, 'post-comments')

urlpatterns = [
    # API Urls
    path('', include(router.urls)),
    path('auth/', jwt_views.TokenObtainPairView.as_view(), name='api_auth'),
    path('auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='api_auth_refresh'),

    path('newsletter-list/', get_newsletter_subs, name='get_newsletter_list'),
]
