from django.contrib import admin
from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["id", "description", "created_at"]
    fields = ["description", "image", "created_at"]
    search_fields = ["description", "created_at"]
    ordering = ["-created_at"]
    readonly_fields = ["created_at"]
