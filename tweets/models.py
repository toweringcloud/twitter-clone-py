from django.db import models
from common.models import Common


class Tweet(Common):

    """Tweet Model Definition"""
    
    payload = models.CharField(
        max_length=180,
        default="",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="tweets",
    )

    def __str__(self):
        return self.payload
    
    def total_likes(self):
        return self.likes.count()


class Like(Common):

    """Like Model Definition"""
    
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="likes",
    )   
    tweet = models.ForeignKey(
        "tweets.Tweet",
        on_delete=models.CASCADE,
        related_name="likes",
    )

    def __str__(self):
        return self.tweet.payload
