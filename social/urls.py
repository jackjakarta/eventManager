from django.urls import path
from . import views


urlpatterns = [
    path('', views.posts_feed, name='posts_feed'),
    path('post/<int:pk>/', views.post_page, name='post_page'),
    path('user/<int:pk>/posts/', views.user_posts, name='user_posts'),
    path('user/<int:pk>/liked-posts/', views.liked_posts, name='liked_posts'),

    path('post/add-post/', views.add_post, name='add_post'),
    path('post/<int:pk>/delete-post/', views.delete_post, name='delete_post'),

    path('post/<int:pk>/like/', views.add_like, name='like_post'),
    path('post/<int:pk>/unlike/', views.delete_like, name='unlike_post'),

    path('post/<int:pk>/add-comment/', views.add_comment, name='add_comment'),
    path('post/<int:pk>/delete-comment/', views.delete_comment, name='delete_comment'),
]
