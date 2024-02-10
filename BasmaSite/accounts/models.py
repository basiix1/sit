from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    address = models.TextField()