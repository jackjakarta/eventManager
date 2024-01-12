from django.contrib import admin
from .models import Venue, Event, Promoter, Profile, NewsletterSub, APIKey, DallEImage


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "zip_code", "city", "website", "email", "created_at", )
    list_filter = ("city", )
    ordering = ("created_at", "name", )
    search_fields = ("name", "city", )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "event_date", "venue", "manager", "created_at", )
    list_filter = ("venue", "manager", )
    ordering = ("created_at", "name", "venue", "manager", "event_date", )
    search_fields = ("name", "venue", "manager", )


@admin.register(Promoter)
class PromoterAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "email", "website", "created_at", )
    list_filter = ("city", )
    ordering = ("created_at", "name", "city", )
    search_fields = ("name", "city", )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at", )
    ordering = ("user", "created_at", )
    search_fields = ("user", )


@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at", )
    ordering = ("user", "created_at", )
    search_fields = ("user", )


@admin.register(DallEImage)
class DallEImageAdmin(admin.ModelAdmin):
    list_display = ("manager", "created_at", )
    ordering = ("manager", "created_at", )
    search_fields = ("manager", )


@admin.register(NewsletterSub)
class NewsletterSubAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at",)
    ordering = ("email", "created_at",)
    search_fields = ("email", )
