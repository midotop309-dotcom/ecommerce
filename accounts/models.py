from django.contrib.auth.models import AbstractUser

from django.db import models 

# Create your models here.

class User(AbstractUser):
    phoneNumber=models.CharField(max_length=11)
    Address=models.TextField()

    def __str__(self):
       return self.username