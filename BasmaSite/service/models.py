from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    created_at = models.DateTimeField(auto_now_add=True)
    icon = models.CharField(max_length=100, default='bx-cart')

class ServiceRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('canceled', 'Canceled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)