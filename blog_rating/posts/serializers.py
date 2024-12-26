from rest_framework import serializers
from .models import Post, Rating

class PostListSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField()
    rating_count = serializers.IntegerField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'average_rating', 'rating_count']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'post', 'score']
