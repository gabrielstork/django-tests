from django.db import models
from accounts.models import Account


class Post(models.Model):
    author = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='account_posts',
    )
    title = models.CharField(max_length=50)
    text = models.TextField()
    likes = models.ManyToManyField(
        Account, blank=True, related_name='liked_posts',
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='account_comments',
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments',
    )
    text = models.TextField()

    def __str__(self):
        return self.text
