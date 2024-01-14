from django.shortcuts import render
from .models import Post


def posts_feed(request):
    posts = Post.objects.all()
    return render(request, "social/posts_feed.html", {
        "posts": posts,
    })


def post_page(request):
    pass
