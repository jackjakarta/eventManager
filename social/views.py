from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post, PostComment

from .forms import PostForm, PostCommentForm


def posts_feed(request):
    if request.user.is_authenticated:
        posts = Post.objects.all().order_by("-created_at")[:10]
        return render(request, "social/posts_feed.html", {
            "posts": posts,
        })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("website:static_pages:home")


def post_page(request, pk):
    if request.user.is_authenticated:
        post = Post.objects.get(id=pk)
        post_comments = PostComment.objects.filter(post_id=pk)
        form = PostCommentForm()

        return render(request, "social/post_page.html", {
            "post": post,
            "comments": post_comments,
            "form": form,
        })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("website:static_pages:home")


def user_posts(request, pk):
    if request.user.is_authenticated:
        posts = Post.objects.filter(user_id=pk)
        return render(request, "social/user_posts.html", {
            "posts": posts,
        })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("website:auth:login")


def liked_posts(request, pk):
    if request.user.is_authenticated:
        posts = Post.objects.filter(likes=pk)
        return render(request, "social/user_liked_posts.html", {
            "posts": posts,
        })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("website:auth:login")


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

        return redirect("post_page", pk=pk)

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

        return redirect("post_page", pk=pk)
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("website:static_pages:home")


def add_comment(request, pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            post = Post.objects.get(pk=pk)
            form = PostCommentForm(request.POST, post=post, user=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "You have added a comment.")
                return redirect("post_page", pk=pk)
            else:
                messages.error(request, "There was a problem adding the comment...")
                return redirect("post_page", pk=pk)
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("website:static_pages:home")


def delete_comment(request):
    pass
