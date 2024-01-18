from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, PostComment

from .forms import PostForm


def posts_feed(request):
    posts = Post.objects.all().order_by("-created_at")[:10]
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
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, user=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "You've created the post successfully.")
                return redirect("posts_feed")
            else:
                messages.error(request, "Your form is not valid.")
                return render(request, "social/add_post.html", {
                    "form": form,
                })
        else:
            form = PostForm()
            return render(request, "social/add_post.html", {
                "form": form,
            })


def delete_post(request, pk):
    if request.user.is_authenticated:
        post = Post.objects.get(id=pk)
        if request.user == post.user:
            post.delete()
            messages.success(request, "Event deleted successfully!")
            return redirect("posts_feed")
        else:
            messages.error(request, "This is not your post. You can't delete it.")
            return redirect("website:static_pages:home")
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("posts_feed")


def add_like(request, pk):
    if request.user.is_authenticated:
        post = Post.objects.get(id=pk)

        if request.user not in post.likes.all():
            post.likes.add(request.user)
            messages.success(request, "You liked this post!")
        else:
            messages.error(request, "You already like this post!")

        return redirect("posts_feed")

    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("website:static_pages:home")


def delete_like(request, pk):
    if request.user.is_authenticated:
        post = Post.objects.get(id=pk)

        if request.user in post.likes.all():
            post.likes.remove(request.user)
            messages.success(request, "You unliked this post")
        else:
            messages.error(request, "You already like this post!")

        return redirect("posts_feed")
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("website:static_pages:home")


def add_comment(request):
    pass


def delete_comment(request):
    pass
