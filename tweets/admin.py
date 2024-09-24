from django.contrib import admin
from .models import Tweet, Like


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("in", "Include Elon Musk"),
            ("ex", "Exclude Elon Musk"),
        ]

    def queryset(self, request, tweets):
        word = self.value()
        print(word)
        if word == "in":
            return tweets.filter(payload__contains="elon musk")
        elif word == "ex":
            return tweets.exclude(payload__contains="elon musk")
        else:
            return tweets


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "payload",
        "created_at",
        "updated_at",
        "total_likes",
    )

    list_filter = (
        WordFilter,
        "created_at",
        "updated_at",
    )

    search_fields = (
        "payload",
        "user__username",
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "created_at",
        "updated_at",
    )

    search_fields = (
        "user__username",
    )
