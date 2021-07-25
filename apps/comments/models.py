from django.db import models
from apps.hotels.models import Hotel
from django.contrib.auth.models import User

# Create your models here.


class Comment(models.Model):
    text = models.TextField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='comment')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='reply_comment', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -- {self.hotel.id}"

    class Meta:
        ordering = ['-comment_created']