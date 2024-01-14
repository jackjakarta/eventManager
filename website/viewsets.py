from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Event, Venue, Promoter
from .serializers import EventSerializer, VenueSerializer, PromoterSerializer


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class VenuesViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class PromotersViewSet(viewsets.ModelViewSet):
    queryset = Promoter.objects.all()
    serializer_class = PromoterSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
