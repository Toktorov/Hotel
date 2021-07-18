from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hotel(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True
    )

    title = models.CharField(
        max_length=255, blank=True
    )

    description = models.TextField(
        blank=True
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.title}"
