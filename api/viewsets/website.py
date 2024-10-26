from django.contrib.auth.models import AnonymousUser
from rest_framework import viewsets, status
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey

from api.serializers.website import (
    EventSerializer,
    VenueSerializer,
    PromoterSerializer,
    ArtistSerializer,
)
from api.serializers.website import NewsletterSubSerializer
from website.models import Event, Venue, Promoter, Artist, NewsletterSub


class ArtistsViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get_queryset(self):
        if not isinstance(self.request.user, AnonymousUser):
            user_id = self.request.user.id

            return Artist.objects.filter(manager_id=user_id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)

    def get_success_headers(self, data):
        try:
            return {"Location": "Yes Yes"}
        except (TypeError, KeyError):
            return {}


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        if not isinstance(self.request.user, AnonymousUser):
            user_id = self.request.user.id

            return Event.objects.filter(manager_id=user_id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)

    def get_success_headers(self, data):
        try:
            return {"Location": "Yes Yes"}
        except (TypeError, KeyError):
            return {}


class VenuesViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

    def get_queryset(self):
        if not isinstance(self.request.user, AnonymousUser):
            user_id = self.request.user.id

            return Venue.objects.filter(manager_id=user_id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)

    def get_success_headers(self, data):
        try:
            return {"Location": "Yes Yes"}
        except (TypeError, KeyError):
            return {}


class PromotersViewSet(viewsets.ModelViewSet):
    queryset = Promoter.objects.all()
    serializer_class = PromoterSerializer

    def get_queryset(self):
        if not isinstance(self.request.user, AnonymousUser):
            user_id = self.request.user.id

            return Promoter.objects.filter(manager_id=user_id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)

    def get_success_headers(self, data):
        try:
            return {"Location": "Yes Yes"}
        except (TypeError, KeyError):
            return {}


# Utility Internal API Endpoint for getting the Newsletter Email List
@api_view(["GET"])
@authentication_classes([])
@permission_classes([HasAPIKey])
def get_newsletter_subs(request):
    email_list = NewsletterSub.objects.all()
    serializer = NewsletterSubSerializer(email_list, many=True)

    return Response(serializer.data)
