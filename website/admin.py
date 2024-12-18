from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .models import Venue, Event, Promoter, Artist, Profile, NewsletterSub


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "country",
        "website",
        "manager",
        "created_at",
    )
    list_filter = ("country",)
    ordering = (
        "name",
        "country",
        "manager",
        "created_at",
    )
    search_fields = (
        "name",
        "country",
        "city",
    )
    readonly_fields = (
        "get_artist_image",
        "created_at",
    )

    fieldsets = (
        (
            _("Artist Image"),
            {
                "fields": (
                    "get_artist_image",
                    "image",
                )
            },
        ),
        (
            _("Artist Contact"),
            {
                "fields": (
                    "name",
                    "email",
                    "website",
                )
            },
        ),
        (
            _("Artist Bio"),
            {
                "fields": (
                    "city",
                    "country",
                    "bio",
                )
            },
        ),
        (
            _("Artist Management"),
            {
                "fields": (
                    "manager",
                    "created_at",
                )
            },
        ),
    )

    def get_artist_image(self, obj):
        if obj.image:
            return format_html('<img src="%s" width="250px" />' % obj.image.url)

    get_artist_image.short_description = "Current Artist Image"


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "address",
        "zip_code",
        "city",
        "country",
        "website",
        "email",
        "created_at",
    )
    list_filter = (
        "city",
        "country",
    )
    ordering = (
        "created_at",
        "name",
    )
    search_fields = (
        "name",
        "city",
        "country",
    )
    readonly_fields = (
        "get_venue_image",
        "updated_at",
    )

    fieldsets = (
        (
            _("Venue Image"),
            {
                "fields": (
                    "get_venue_image",
                    "image",
                )
            },
        ),
        (
            _("Venue Contact Information"),
            {
                "fields": (
                    "name",
                    "address",
                    "zip_code",
                    "city",
                    "country",
                    "email",
                    "website",
                )
            },
        ),
        (
            _("Venue Management"),
            {
                "fields": (
                    "manager",
                    "updated_at",
                )
            },
        ),
    )

    def get_venue_image(self, obj):
        if obj.image:
            return format_html('<img src="%s" width="250px" />' % obj.image.url)

    get_venue_image.short_description = "Current Venue Image"


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "event_date",
        "venue",
        "event_type",
        "manager",
        "get_event_flyer",
        "created_at",
    )
    list_filter = (
        "event_type",
        "venue",
        "promoter",
        "artists",
        "genre",
    )
    ordering = (
        "created_at",
        "name",
        "venue",
        "event_type",
        "manager",
        "event_date",
    )
    search_fields = (
        "name",
        "venue",
        "manager",
        "event_type",
    )
    readonly_fields = (
        "get_event_flyer",
        "get_event_flyer_big",
        "attendees",
    )

    fieldsets = (
        (
            _("Event Flyer"),
            {
                "fields": (
                    "get_event_flyer_big",
                    "event_flyer",
                )
            },
        ),
        (
            _("Event Information"),
            {
                "fields": (
                    "name",
                    "event_date",
                    "description",
                    "event_type",
                    "genre",
                )
            },
        ),
        (
            _("Event Management"),
            {
                "fields": (
                    "manager",
                    "venue",
                    "promoter",
                    "artists",
                )
            },
        ),
        (_("Event Attendees"), {"fields": ("attendees",)}),
    )

    def get_event_flyer(self, obj):
        if obj.event_flyer:
            return format_html('<img src="%s" width="50px" />' % obj.event_flyer.url)

    get_event_flyer.short_description = "Current Event Flyer"

    def get_event_flyer_big(self, obj):
        if obj.event_flyer:
            return format_html('<img src="%s" width="250px" />' % obj.event_flyer.url)

    get_event_flyer_big.short_description = "Current Event Flyer"


@admin.register(Promoter)
class PromoterAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "city",
        "email",
        "website",
        "created_at",
    )
    list_filter = ("city",)
    ordering = (
        "created_at",
        "name",
        "city",
    )
    search_fields = (
        "name",
        "city",
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "display_avatar",
        "fav_genre",
        "fav_artist",
        "created_at",
    )
    list_filter = (
        "fav_genre",
        "fav_artist",
    )
    ordering = (
        "user",
        "fav_genre",
        "created_at",
    )
    search_fields = ("fav_genre",)
    readonly_fields = (
        "display_avatar",
        "display_avatar_big",
        "user",
        "user_name",
    )

    fieldsets = (
        (
            _("Avatar"),
            {
                "fields": (
                    "display_avatar_big",
                    "avatar",
                )
            },
        ),
        (
            _("Contact Information"),
            {
                "fields": (
                    "user_name",
                    "user",
                )
            },
        ),
        (
            _("Profile Information"),
            {
                "fields": (
                    "fav_genre",
                    "fav_artist",
                )
            },
        ),
    )

    def user_name(self, obj):
        if obj.user.first_name:
            return f"{obj.user.first_name} {obj.user.last_name}"

    user_name.short_description = "Full Name"

    def display_avatar(self, obj):
        if obj.avatar:
            return format_html('<img src="%s" width="50px" />' % obj.avatar.url)

    display_avatar.short_description = "Current Avatar"

    def display_avatar_big(self, obj):
        if obj.avatar:
            return format_html('<img src="%s" width="250px" />' % obj.avatar.url)

    display_avatar_big.short_description = "Current Avatar"


@admin.register(NewsletterSub)
class NewsletterSubAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "created_at",
    )
    ordering = (
        "email",
        "created_at",
    )
    search_fields = ("email",)
