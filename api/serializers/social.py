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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["user"] = instance.user.email
        representation["likes"] = instance.likes.count()
        representation["event"] = instance.event.name if instance.event else "No Event"

        return representation


class PostCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = PostComment
        exclude = ["updated_at", ]
