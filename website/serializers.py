from rest_framework import serializers
from .models import Event, Venue, Promoter
from django.contrib.auth import get_user_model

AuthUser = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        exclude = [
            "last_login",
            "password",
            "is_superuser",
            "is_staff",
            "groups",
            "user_permissions",
        ]


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
    promoter = PromoterSerializer()
    manager = UserSerializer()

    class Meta:
        model = Event
        exclude = []
        depth = 1
