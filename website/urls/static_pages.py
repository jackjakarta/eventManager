from django.urls import path
from website.views.static import home, app_docs, app_docs_api, privacy_policy, contact

app_name = 'static_pages'


urlpatterns = [
    # Static Pages
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('docs/', app_docs, name='docs'),  # Not implemented
    path('docs/api/', app_docs_api, name='docs_api'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
]
