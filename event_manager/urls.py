from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

import website.viewsets as wb_views

router = routers.DefaultRouter()
router.register(r'events', wb_views.EventsViewSet, 'events')
router.register(r'venues', wb_views.VenuesViewSet, 'venues')
router.register(r'promoters', wb_views.PromotersViewSet, 'promoters')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('social/', include('social.urls')),

    path('api/', include(router.urls)),
    path('api/auth/', jwt_views.TokenObtainPairView.as_view(), name='api_auth'),
    path('api/auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='api_auth_refresh'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
