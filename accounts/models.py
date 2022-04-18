from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    followers = models.ManyToManyField(
        'self', blank=True, symmetrical=False, related_name='account_followers',
    )
    following = models.ManyToManyField(
        'self', blank=True, symmetrical=False, related_name='account_following',
    )

    def __str__(self):
        return self.username
