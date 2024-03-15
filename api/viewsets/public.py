from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response

from api.serializers.public import PublicArtistSerializer, PublicPromoterSerializer, PublicVenueSerializer
from api.serializers.public import PublicEventSerializer
from website.models import Artist, Event, Promoter, Venue


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def get_artists(request):
    artists_list = Artist.objects.all()
    serializer = PublicArtistSerializer(artists_list, many=True)

    return Response(serializer.data)


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def get_events(request):
    events_list = Event.objects.all()
    serializer = PublicEventSerializer(events_list, many=True)

    return Response(serializer.data)


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def get_promoters(request):
    promoters_list = Promoter.objects.all()
    serializer = PublicPromoterSerializer(promoters_list, many=True)

    return Response(serializer.data)


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def get_venues(request):
    venues_list = Venue.objects.all()
    serializer = PublicVenueSerializer(venues_list, many=True)

    return Response(serializer.data)
