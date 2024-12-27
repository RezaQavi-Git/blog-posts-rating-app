import datetime
from celery import shared_task
from django.db.models import Avg, Count
from .models import Post
import logging

logger = logging.getLogger(__name__)

@shared_task
def update_post_metrics():
    logger.info(f'Task update_post_metrics is running {datetime.time} ...')
    posts = Post.objects.all()
    for post in posts:
        post.average_rating = post.ratings.aggregate(Avg('score'))['score__avg'] or 0
        post.rating_count = post.ratings.count()
        post.save()
