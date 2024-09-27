from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from tweets.serializers import TweetSerializer
from .models import User
from .serializers import UserSerializer


class Users(APIView):
    def get(self, request):
        all_users = User.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return Response(serializer.data)


class UserDetail(APIView):
    def get_object(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise NotFound

    def get(self, request, user_id):
        serializer = UserSerializer(self.get_object(user_id))
        return Response(serializer.data)


class UserTweets(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
            serializer = TweetSerializer(user.tweets, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            raise NotFound
