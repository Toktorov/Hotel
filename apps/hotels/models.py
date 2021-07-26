from django.db import models
from django.contrib.auth.models import User
from apps.categories.models import Category

# Create your models here.
class Hotel(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True
    )

    title = models.CharField(
        max_length=255, 
        blank=True,
        verbose_name='Название:'
    )

    description = models.TextField(
        blank=True,
        verbose_name='Описание:'
    )

    price = models.PositiveIntegerField(
        verbose_name='Цена за сутки:',
        default = 0
        )

    wifi = models.CharField(
        max_length=10, 
        blank=True, 
        default = 'Нет',
        verbose_name='Wifi:'
    )

    parking = models.CharField(
        max_length=20, 
        blank=True, 
        default = 'Нет',
        verbose_name='Парковка:'
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    category = models.ForeignKey(
        Category,
        related_name='hotel_category',
        on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name='Категория:'
    )

    def __str__(self):
        return f"{self.title}"

class HotelImage(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name='hotel_image'
    )

    image = models.ImageField(
        upload_to='hotel_image',
        verbose_name='Фото отеля'
    )

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes_user')
    hotels = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='likes_hotel')


    def __str__(self):
        return f"{self.id}"