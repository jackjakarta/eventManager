from django.urls import path
from website.views.static import home, app_docs, app_docs_api

app_name = 'static_pages'


urlpatterns = [
    # Static Pages
    path('', home, name='home'),
    path('docs/', app_docs, name='docs'),  # Not implemented
    path('docs/api/', app_docs_api, name='docs_api'),
]
