from django.urls import path
from . import views


# GET /api/v1/tweets
# POST /api/v1/tweets
# GET /api/v1/tweets/<int:pk>
# PUT /api/v1/tweets/<int:pk>
# DELETE /api/v1/tweets/<int:pk>
urlpatterns = [
    path("", views.Tweets.as_view()),
    path("<int:pk>", views.TweetDetail.as_view()),
]
