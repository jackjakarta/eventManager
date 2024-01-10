from django.contrib import admin
from .models import Venue, Event, Promoter, Profile, NewsletterSub, APIKey


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "zip_code", "city", "website", "email", )
    list_filter = ("city", )
    ordering = ("created_at", "name", )
    search_fields = ("name", "city", )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "venue", "manager", "event_date", )
    list_filter = ("venue", "manager", )
    ordering = ("created_at", "name", "venue", "manager", )
    search_fields = ("name", "venue", "manager", )


@admin.register(Promoter)
class PromoterAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "email", "website")
    list_filter = ("city", )
    ordering = ("created_at", "name", "city", )
    search_fields = ("name", "city", )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", )
    ordering = ("created_at", )
    search_fields = ("user", )


admin.site.register(APIKey)


@admin.register(NewsletterSub)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at",)
    ordering = ("email", "created_at",)
    search_fields = ("email", )
