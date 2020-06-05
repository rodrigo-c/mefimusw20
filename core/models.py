from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Group(models.Model):
    title = models.CharField(max_length=200)

class Submission(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group, blank=True)
    title = models.CharField(max_length=1000)
    text = models.TextField(blank=True)
    link = models.URLField(blank=True)
    cover_image = models.ImageField(upload_to='covers', blank=True)
    back_image = models.ImageField(upload_to='covers', blank=True)
    tags = models.CharField(max_length=1000)

class Comment(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submission = models.ForeignKey('Submission', on_delete=models.CASCADE)
    body = models.TextField()
