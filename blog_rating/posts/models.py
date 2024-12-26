from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

    @property
    def average_rating(self):
        return self.ratings.aggregate(avg=models.Avg('score'))['avg'] or 0

    @property
    def rating_count(self):
        return self.ratings.count()

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='ratings', on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f'{self.user.username} - {self.post.title} - {self.score}'
