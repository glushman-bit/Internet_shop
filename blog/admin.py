from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "image", "created_at", "is_active",)
    list_filter = ("title", "created_at", "is_active",)
    search_fields = ("title", "created_at", "is_active",)
