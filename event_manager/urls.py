from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

import website.views as views

router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet, 'events')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),

    path('api/', include(router.urls)),
    path('api/auth/', jwt_views.TokenObtainPairView.as_view(), name='api-auth'),
    path('api/auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='api-auth-refresh'),
]
