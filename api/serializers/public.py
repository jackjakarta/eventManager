from rest_framework import serializers

from website.models import Artist, Event, Promoter, Venue


class PublicArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        exclude = [
            "created_at",
            "updated_at",
            "manager",
        ]


class PublicVenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        exclude = [
            "created_at",
            "updated_at",
            "manager",
        ]


class PublicPromoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promoter
        exclude = [
            "created_at",
            "updated_at",
            "manager",
        ]


class PublicEventSerializer(serializers.ModelSerializer):
    venue = PublicVenueSerializer()
    promoter = PublicPromoterSerializer()
    artists = PublicArtistSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        exclude = [
            "created_at",
            "manager",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["attendees"] = instance.attendees.count()
        return representation
