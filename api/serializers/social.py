from rest_framework import serializers

from api.serializers.website import UserSerializer, EventSerializer
from social.models import Post, PostComment


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    event = EventSerializer()
    likes = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        exclude = ["updated_at", ]


class PostCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = PostComment
        exclude = ["updated_at", ]
