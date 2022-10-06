from django.db import models
from django.conf import settings


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    issue_a = models.CharField(max_length=100)
    issue_b = models.CharField(max_length=100)

class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    pick = models.BooleanField(default=False)
    content = models.CharField(max_length=100)   