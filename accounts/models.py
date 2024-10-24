from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='avatars')
    
    def str(self):
        return self.username