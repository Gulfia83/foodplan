from django.contrib.auth.models import AbstractUser
from django.db import models

from recipeapp.models import Dish


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='avatars')
    
    def str(self):
        return self.username
    

class Like(models.Model):
    user = models.ForeignKey(CustomUser, related_name='likes', verbose_name='Лайк', on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, related_name='likes', verbose_name='Лайк', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'dish'], name="unique_like"),
        ]

    def __str__(self):
        return f"{self.user} liked {self.dish} on {self.created_at}"