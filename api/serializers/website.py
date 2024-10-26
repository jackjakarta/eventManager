from django.contrib.auth import get_user_model
from rest_framework import serializers

from website.models import Event, Venue, Promoter, Artist, NewsletterSub

AuthUser = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        exclude = [
            "id",
            "last_login",
            "password",
            "is_superuser",
            "is_staff",
            "is_active",
            "is_newsletter_sub",
            "date_joined",
            "groups",
            "user_permissions",
        ]


class ArtistSerializer(serializers.ModelSerializer):
    # manager = UserSerializer()
    manager = serializers.PrimaryKeyRelatedField(
        queryset=AuthUser.objects.all(), required=False
    )

    class Meta:
        model = Artist
        exclude = [
            "created_at",
            "updated_at",
        ]
        depth = 1

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        manager = instance.manager
        if manager:
            representation["manager"] = UserSerializer(manager).data
        return representation


class VenueSerializer(serializers.ModelSerializer):
    manager = serializers.PrimaryKeyRelatedField(
        queryset=AuthUser.objects.all(), required=False
    )

    class Meta:
        model = Venue
        exclude = [
            "created_at",
            "updated_at",
        ]
        depth = 1

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        manager = instance.manager
        if manager:
            representation["manager"] = UserSerializer(manager).data
        return representation


class PromoterSerializer(serializers.ModelSerializer):
    manager = serializers.PrimaryKeyRelatedField(
        queryset=AuthUser.objects.all(), required=False
    )

    class Meta:
        model = Promoter
        exclude = [
            "created_at",
            "updated_at",
        ]
        depth = 1

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        manager = instance.manager
        if manager:
            representation["manager"] = UserSerializer(manager).data
        return representation


class EventSerializer(serializers.ModelSerializer):
    venue = VenueSerializer()
    artists = ArtistSerializer(many=True, read_only=True)
    promoter = PromoterSerializer()
    manager = serializers.PrimaryKeyRelatedField(
        queryset=AuthUser.objects.all(), required=False
    )
    attendees = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        exclude = []
        depth = 1


class NewsletterSubSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSub
        exclude = [
            "created_at",
            "updated_at",
        ]
