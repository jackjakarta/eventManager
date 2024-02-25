from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Apps Urls
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('social/', include('social.urls')),
    path('activation/', include('users.urls')),
    path('api/', include('api.urls')),
]


if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
