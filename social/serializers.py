from rest_framework import serializers
from .models import Post, PostComment
from website.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Post
        exclude = ["updated_at", ]


class PostCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = PostComment
        exclude = ["updated_at", ]
