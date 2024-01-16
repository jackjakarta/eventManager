from django.urls import path
from website.views import ai_assistant_event, ai_assistant_image


app_name = 'api_calls'

urlpatterns = [
    # AI API Calls
    path('assistant/', ai_assistant_event, name='assistant'),
    path('assistant/flyer-generator/', ai_assistant_image, name='assistant_image'),
]