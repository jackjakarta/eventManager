from django.shortcuts import render


def posts_feed(request):
    return render(request, "social/posts_feed.html")


def post_page(request):
    pass
