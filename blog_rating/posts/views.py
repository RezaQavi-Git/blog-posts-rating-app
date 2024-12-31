from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from .models import Post, Rating
from .serializers import PostListSerializer, RatingSerializer

class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class RatingCreateUpdateView(generics.CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        try:
            rating = Rating.objects.get(user=user, post_id=data['post'])
            rating.score = data['score']
            rating.save()
            return Response({'message': 'Rating updated successfully'}, status=status.HTTP_200_OK)
        except Rating.DoesNotExist:
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)
            return Response({'message': 'Rating created successfully'}, status=status.HTTP_201_CREATED)
