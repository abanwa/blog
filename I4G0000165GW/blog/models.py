from cgitb import text
from datetime import date
from turtle import title
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title