from django.urls import path
from . import views


# GET /api/v1/users
# GET /api/v1/users/<int:pk>
# GET /api/v1/users/<int:pk>/tweets
urlpatterns = [
    path("", views.Users.as_view()),
    path("<int:pk>", views.UserDetail.as_view()),
    path("<int:pk>/tweets", views.UserTweets.as_view()),
]
