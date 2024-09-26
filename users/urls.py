from django.urls import path
from . import views

urlpatterns = [
    path("", views.users),
    path("<int:user_id>", views.user),
    path("<int:user_id>/tweets", views.tweets),
]