from celery import shared_task
from django.db.models import Avg, Count
from .models import Post

@shared_task
def update_post_metrics():
    print("here")
    posts = Post.objects.all()
    for post in posts:
        post.average_rating = post.ratings.aggregate(Avg('score'))['score__avg'] or 0
        post.rating_count = post.ratings.count()
        post.save()
