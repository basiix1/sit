from django.db import models
from django.forms import TimeField, TimeInput
from django.utils import timezone
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    date_added = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(User, max_length=255)



    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f'{self.name} - {self.project.title}'

class Rating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings')
    stars = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    