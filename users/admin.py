from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from rest_framework_api_key.admin import APIKeyModelAdmin

from .models import AuthUser, UserAPIKey, Activation


@admin.register(AuthUser)
class AuthUserAdmin(BaseUserAdmin):
    ordering = ("email",)
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'id')
    search_fields = ('email', 'first_name', 'last_name')

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name", "email", "password1", "password2"),
            },
        ),
    )


@admin.register(UserAPIKey)
class UserAPIKeyModelAdmin(APIKeyModelAdmin):
    list_display = [*APIKeyModelAdmin.list_display, "user"]
    search_fields = [*APIKeyModelAdmin.search_fields, "user__email"]


@admin.register(Activation)
class ActivationAdmin(admin.ModelAdmin):
    list_display = ("user", "token", "expires_at", "activated_at", )
    ordering = ("user", )
    readonly_fields = ("user", "token", "expires_at", "activated_at", )

    fieldsets = (
        (_("Activation Information"), {"fields": ("user", "token", "expires_at", "activated_at", )}),
    )
