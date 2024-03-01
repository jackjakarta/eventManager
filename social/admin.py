from django.contrib import admin
from .models import Post, PostComment
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user", "get_post_image", "description", "event", "get_post_like_count", )
    ordering = ("user", "event", )
    search_fields = ("description", )
    readonly_fields = ("get_post_image", "get_post_image_big", "created_at", "user", "likes", "get_post_like_count", )

    fieldsets = (
        (_("Post Image"), {"fields": ("get_post_image_big", "image", )}),
        (_("Post Information"), {"fields": ("event", "description", )}),
        (_("Post Management"), {"fields": ("user", "created_at", "get_post_like_count", )}),
    )

    def get_post_image(self, obj):
        if obj.image:
            return format_html('<img src="%s" width="50px" />' % obj.image.url)
    get_post_image.short_description = "Post Image"

    def get_post_image_big(self, obj):
        if obj.image:
            return format_html('<img src="%s" width="250px" />' % obj.image.url)
    get_post_image_big.short_description = "Post Image"

    def get_post_like_count(self, obj):
        if obj.likes:
            return obj.likes.count()
        else:
            return 0

    get_post_like_count.short_description = "Likes"


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ("post", "text", )
    ordering = ("user", "post", "text", )
    search_fields = ("user", "post", "text", )
    readonly_fields = ("user", "post", )

    fieldsets = (
        (_("Comment"), {"fields": ("text", )}),
        (_("Post Information"), {"fields": ("user", "post", )})
    )
