from django.contrib import admin
from .models import Tweet, Like


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "payload",
        "created_at",
        "updated_at"
    )
    
    list_filter = (
        "created_at",
        "updated_at"       
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "updated_at"
    )
    
    list_filter = (
        "created_at",
        "updated_at"       
    )
