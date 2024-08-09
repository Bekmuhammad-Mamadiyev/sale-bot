from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram = models.CharField(null=True, blank=True, max_length=255)
    instagram = models.CharField(null=True, blank=True, max_length=255)
    bio = models.CharField(null=True, blank=True, max_length=200)
    age = models.IntegerField(default=0)
    job = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return self.user.first_name