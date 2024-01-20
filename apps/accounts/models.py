from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150, unique = True)
    profile_photo = models.ImageField(upload_to='images/profile_photos')

    def __str__(self):
        return self.username