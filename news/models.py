
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import datetime, date

# Create your models here.

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('news:list')

class NewsModel(models.Model):

    title = models.CharField(max_length=200)
    # Delete this if user is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=100, default='General')

    def __str__(self):
        return self.title + '-' + str(self.author)

    def get_absolute_url(self):
        return reverse('news:detail', args=(str(self.id)))

