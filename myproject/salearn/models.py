from django.db import models

# Create your models here.

class UserProfile(models.Model):
    Username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

