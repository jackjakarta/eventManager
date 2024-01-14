from django.shortcuts import render
# from .models import Article


def blog_home(request):
    # articles = Article.objects.all()
    return render(request, "blog/blog_home.html", {
        # "articles": articles,
    })
