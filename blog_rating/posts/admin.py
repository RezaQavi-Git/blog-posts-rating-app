from django.contrib import admin
from .models import Post, Rating

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'average_rating', 'rating_count')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'score')
    list_filter = ('score',)
    search_fields = ('user__username', 'post__title')
