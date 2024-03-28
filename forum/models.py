from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    body = models.CharField(max_length=1000)
    likes = models.IntegerField(default=0)


class Comment(models.Model):
    post = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
