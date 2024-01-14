from django.shortcuts import render
from .models import Post, PostComment


def posts_feed(request):
    posts = Post.objects.all()
    return render(request, "social/posts_feed.html", {
        "posts": posts,
    })


def post_page(request):
    pass


def user_posts(request, pk):
    pass


def liked_posts(request, pk):
    pass


def add_post(request):
    pass


def delete_post(request):
    pass


def add_like(request):
    pass


def delete_like(request):
    pass


def add_comment(request):
    pass


def delete_comment(request):
    pass
