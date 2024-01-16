from django.urls import path
from website.views.utillity import send_test_email, send_newsletter_email, subscribe_newsletter


app_name = 'utility'

urlpatterns = [
    # Utility Views
    path('send-test-email/', send_test_email, name='send_test_email'),
    path('send-newsletter/', send_newsletter_email, name='send_newsletter_email'),
    path('subscribe-newsletter/', subscribe_newsletter, name='subscribe_newsletter'),
]
