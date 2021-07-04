from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100) 
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    thumb = models.ImageField(default=None, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    upvotes = models.IntegerField(default=0)
    liked_by = models.ManyToManyField(User, related_name='likes')
    disliked_by = models.ManyToManyField(User, related_name='dislikes')
    downvotes = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50] + '...'