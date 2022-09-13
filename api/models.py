from django.db import models

class urlShortener(models.Model):
    longURL = models.CharField(max_length=255)
    shortURL = models.CharField(max_length=10)

    def __str__(self):
        return self.shortURL