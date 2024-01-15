from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Event, Venue, Promoter
from .serializers import EventSerializer, VenueSerializer, PromoterSerializer


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [HasAPIKey | IsAuthenticated]
    authentication_classes = (JWTAuthentication, )


class VenuesViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    permission_classes = [HasAPIKey | IsAuthenticated]
    authentication_classes = (JWTAuthentication, )


class PromotersViewSet(viewsets.ModelViewSet):
    queryset = Promoter.objects.all()
    serializer_class = PromoterSerializer
    permission_classes = [HasAPIKey | IsAuthenticatedOrReadOnly]
    authentication_classes = (JWTAuthentication, )
