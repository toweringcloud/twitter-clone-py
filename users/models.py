from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    name = models.CharField(
        max_length=150,
        blank=True,
    )
    avatar = models.ImageField(
        blank=True,
    )

    def __str__(self):
        return self.username

    def total_tweets(self):
        return self.tweets.count()

    def total_likes(self):
        return self.likes.count()
