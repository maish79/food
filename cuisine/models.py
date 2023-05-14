from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField


class Cuisine(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    image = CloudinaryField('image', default='https://res.cloudinary.com/dlclpbfkf/image/upload/v1680545745/food-placeholder_j41avo.png')
    ingredients = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("cuisine-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    def get_comments(self):
        return self.comments.order_by('-created_date')


class Comment(models.Model):
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.cuisine}"


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return self.name
