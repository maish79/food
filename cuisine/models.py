from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Cuisine(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    ingredients = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("cuisine-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.cuisine}"
