from django.db import models

from urlshortener.validators import validate_url


class UrlShortener(models.Model):
    created_data = models.DateTimeField(auto_now_add=True)
    original_url = models.CharField(max_length=250, validators=[validate_url])
    short_url = models.TextField(unique=True)
    counter = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.original_url} to {self.short_url}'
