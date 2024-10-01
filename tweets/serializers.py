from rest_framework.serializers import ModelSerializer

from users.serializers import TinyUserSerializer
from .models import Tweet


class TweetSerializer(ModelSerializer):
    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = "__all__"
