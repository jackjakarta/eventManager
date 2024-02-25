from django.contrib import admin
from .models import Venue, Event, Promoter, Artist, Profile, NewsletterSub, DallEImage
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass


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
    list_display = ("user", "display_avatar", "fav_genre", "created_at", )
    list_filter = ("fav_genre", )
    ordering = ("user", "fav_genre", "created_at", )
    search_fields = ("fav_genre", )
    readonly_fields = ("display_avatar", "user", "user_name", )

    fieldsets = (
        (_("Avatar"), {"fields": ("display_avatar", "avatar",)}),
        (_("Contact Information"), {"fields": ("user_name", "user", )}),
        (_("Profile Information"), {"fields": ("fav_genre", )}),
    )

    def user_name(self, obj):
        if obj.user.first_name:
            return f"{obj.user.first_name} {obj.user.last_name}"

    user_name.short_description = "Full Name"

    def display_avatar(self, obj):
        if obj.avatar:
            return format_html('<img src="%s" width="50px" />' % obj.avatar.url)

    display_avatar.short_description = "Current Avatar"


# @admin.register(DallEImage)
# class DallEImageAdmin(admin.ModelAdmin):
#     list_display = ("manager", "created_at", )
#     ordering = ("manager", "created_at", )
#     search_fields = ("manager", )


@admin.register(NewsletterSub)
class NewsletterSubAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at",)
    ordering = ("email", "created_at",)
    search_fields = ("email", )
