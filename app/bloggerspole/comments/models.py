from django.db import models
from django.contrib.auth.models import User
from blogs.models import Blog

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
