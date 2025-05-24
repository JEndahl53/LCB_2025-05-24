# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    """
    # Add any additional fields you want to include in your custom user model
    # For example, you can add a profile picture field:
    # profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    pass

    def __str__(self):
        return self.username
