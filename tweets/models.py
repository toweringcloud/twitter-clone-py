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
    )

    def __str__(self) -> str:
        return "Tweet Model"


class Like(Common):

    """Like Model Definition"""
    
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )   
    tweet = models.ForeignKey(
        "tweets.Tweet",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return "Like Model"
