
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()
class NewsModel(models.Model):

    title = models.CharField(max_length=200)
    # Delete this if user is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + '-' + str(self.author)

