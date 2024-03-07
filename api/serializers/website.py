from django.contrib.auth import get_user_model
from rest_framework import serializers

from website.models import Event, Venue, Promoter, Artist, NewsletterSub

AuthUser = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        exclude = [
            "last_login",
            "password",
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
            "groups",
            "user_permissions",
        ]


class ArtistSerializer(serializers.ModelSerializer):
    manager = UserSerializer()

    class Meta:
        model = Artist
        exclude = ["created_at", "updated_at", ]
        depth = 1


class VenueSerializer(serializers.ModelSerializer):
    manager = UserSerializer()

    class Meta:
        model = Venue
        exclude = ["created_at", "updated_at", ]
        depth = 1


class PromoterSerializer(serializers.ModelSerializer):
    manager = UserSerializer()

    class Meta:
        model = Promoter
        exclude = ["created_at", "updated_at", ]
        depth = 1


class EventSerializer(serializers.ModelSerializer):
    venue = VenueSerializer()
    artists = ArtistSerializer(many=True, read_only=True)
    promoter = PromoterSerializer()
    manager = UserSerializer()
    attendees = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        exclude = []
        depth = 1


class NewsletterSubSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSub
        exclude = ["created_at", "updated_at", "id", ]
