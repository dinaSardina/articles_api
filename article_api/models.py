from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    author = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    body = models.TextField()
    public = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} ({self.author})'

    class Meta:
        ordering = ['-created']

