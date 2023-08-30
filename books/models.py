from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='media/', blank=True, null=True)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
