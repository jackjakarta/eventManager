from rest_framework import serializers
from .models import Post, PostComment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = []


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        exclude = []

