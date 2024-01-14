from django.urls import path
from . import views


urlpatterns = [
    path('', views.posts_feed, name='posts_feed'),
    path('posts/<int:pk>/', views.post_page, name='post_page'),
]
