from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from tweets.serializers import TweetSerializer
from .models import User
from .serializers import PrivateUserSerializer, TinyUserSerializer


class Me(APIView):
    permission_classes = [IsAuthenticated]

    # GET /api/v1/users/me
    def get(self, request):
        user = request.user
        serializer = PrivateUserSerializer(user)
        return Response(serializer.data)

    # PUT /api/v1/users/me
    def put(self, request):
        user = request.user
        serializer = PrivateUserSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class Users(APIView):
    # GET /api/v1/users
    def get(self, request):
        all_users = User.objects.all()
        serializer = TinyUserSerializer(all_users, many=True)
        return Response(serializer.data)

    # POST /api/v1/users
    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise ParseError
        serializer = PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class UserDetail(APIView):
    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound

    # GET /api/v1/users/<str:username>
    def get(self, request, username):
        user = self.get_object(username)
        serializer = PrivateUserSerializer(user)
        return Response(serializer.data)

    # PUT /api/v1/users/<srt:username>
    def put(self, request, username):
        user = self.get_object(username)
        serializer = PrivateUserSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class UserTweets(APIView):
    # GET /api/v1/users/<int:pk>/tweets
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = TweetSerializer(user.tweets, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            raise NotFound


class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    # PUT /api/v1/users/password
    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        if not old_password or not new_password:
            raise ParseError
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            raise ParseError


class LogIn(APIView):
    # POST /api/v1/users/login
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            login(request, user)
            return Response({"ok": "Welcome!"})
        else:
            return Response({"error": "wrong password"})


class LogOut(APIView):
    permission_classes = [IsAuthenticated]

    # POST /api/v1/users/logout
    def post(self, request):
        logout(request)
        return Response({"ok": "bye!"})
