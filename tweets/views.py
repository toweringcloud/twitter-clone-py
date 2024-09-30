from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from .models import Tweet
from .serializers import TweetSerializer


class Tweets(APIView):
    # GET /api/v1/tweets
    def get(self, request):
        all_tweets = Tweet.objects.all()
        serializer = TweetSerializer(all_tweets, many=True)
        return Response(serializer.data)

    # POST /api/v1/tweets
    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            new_tweet = serializer.save()
            return Response(
                TweetSerializer(new_tweet).data,
            )
        else:
            return Response(serializer.errors)


class TweetDetail(APIView):
    def get_object(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound

    # GET /api/v1/tweets/<int:pk>
    def get(self, request, pk):
        serializer = TweetSerializer(self.get_object(pk))
        return Response(serializer.data)

    # PUT /api/v1/tweets/<int:pk>
    def put(self, request, pk):
        serializer = TweetSerializer(
            self.get_object(pk),
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_tweet = serializer.save()
            return Response(
                TweetSerializer(updated_tweet).data,
            )
        else:
            return Response(serializer.errors)

    # DELETE /api/v1/tweets/<int:pk>
    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)
