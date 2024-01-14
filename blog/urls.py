from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    # path('article/<int:pk>/', views.article, name='article'),
]
