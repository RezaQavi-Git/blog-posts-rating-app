from django.urls import path
from .views import PostListView, RatingCreateUpdateView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('ratings/', RatingCreateUpdateView.as_view(), name='rating-create-update'),
]
