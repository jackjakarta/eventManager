from rest_framework import serializers

from api.serializers.website import UserSerializer
from social.models import Post, PostComment


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
