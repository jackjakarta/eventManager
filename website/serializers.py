from rest_framework import serializers
from .models import Event, Venue, Promoter


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ["created_at", "updated_at", ]
        depth = 1


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        exclude = ["created_at", "updated_at", ]


class PromoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promoter
        exclude = ["created_at", "updated_at", ]
