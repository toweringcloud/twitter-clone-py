from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet

def read_tweets(request):
    tweets = Tweet.objects.all()
    return render(
        request, 
        "all_tweets.html",
        {
            "tweets": tweets,
            "title": "Tweet List",
        }
    )
