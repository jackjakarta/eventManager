from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from users.utils.decorators import user_is_authenticated
from .forms import PostForm, PostCommentForm
from .models import Post, PostComment


@user_is_authenticated
def posts_feed(request):
    posts = Post.objects.all().order_by("-created_at")[:10]
    return render(request, "social/posts_feed.html", {
        "posts": posts,
    })


@user_is_authenticated
def post_page(request, pk):
    post = get_object_or_404(Post, id=pk)
    post_comments = PostComment.objects.filter(post_id=pk)
    form = PostCommentForm()

    return render(request, "social/post_page.html", {
        "post": post,
        "comments": post_comments,
        "form": form,
    })


@user_is_authenticated
def user_posts(request, pk):
    posts = Post.objects.filter(user_id=pk)
    return render(request, "social/user_posts.html", {
        "posts": posts,
    })


@user_is_authenticated
def liked_posts(request, pk):
    posts = Post.objects.filter(likes=pk)
    return render(request, "social/user_liked_posts.html", {
        "posts": posts,
    })


@user_is_authenticated
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, user=request.user)

        if form.is_valid() and form.check_for_moderation():
            form.save()
            messages.success(request, "You've created the post successfully.")
            return redirect("posts_feed")
        else:
            messages.error(request, "Your form is not valid or contains harmful language.")
            return render(request, "social/add_post.html", {
                "form": form,
            })
    else:
        form = PostForm()
        return render(request, "social/add_post.html", {
            "form": form,
        })


@user_is_authenticated
def delete_post(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.user == post.user:
        post.delete()
        messages.success(request, "Event deleted successfully!")
        return redirect("posts_feed")
    else:
        messages.error(request, "This is not your post. You can't delete it.")
        return redirect("website:static_pages:home")


@user_is_authenticated
def add_like(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.user not in post.likes.all():
        post.likes.add(request.user)
        messages.success(request, "You liked this post!")
    else:
        messages.error(request, "You already like this post!")

    return redirect("post_page", pk=pk)


@user_is_authenticated
def delete_like(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
        messages.success(request, "You unliked this post")
    else:
        messages.error(request, "You already like this post!")

    return redirect("post_page", pk=pk)


@user_is_authenticated
def add_comment(request, pk):
    if request.method == "POST":
        post = get_object_or_404(Post, id=pk)
        form = PostCommentForm(request.POST, post=post, user=request.user)

        if form.is_valid() and form.check_for_moderation():
            form.save()
            messages.success(request, "You have added a comment.")
            return redirect("post_page", pk=pk)
        else:
            messages.error(request, "Your form is not valid or contains harmful language.")
            return redirect("post_page", pk=pk)


def delete_comment(request):
    pass
