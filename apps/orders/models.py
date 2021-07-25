from django.db import models
from apps.hotels.models import Hotel
from django.contrib.auth.models import User
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True
    )
    
    order = models.ForeignKey(
        Hotel, 
        on_delete=models.CASCADE, 
        related_name='order'
    )

    create_at = models.DateTimeField(
        auto_now_add=True
    )
    
    arrival_date = models.DateTimeField(
        verbose_name='Дата заезда:'
    )

    departure_date = models.DateTimeField(
        verbose_name='Дата отъезда:',
    )

    name = models.CharField(
        max_length=50,
         verbose_name='Имя:'
    )

    surname = models.CharField(
        max_length=50,
         verbose_name='Фамилия:'
    )

    fatherland = models.CharField(
        max_length = 50,
         verbose_name='Отечество:',
    )

    id_card = models.PositiveIntegerField(
        verbose_name='Паспорт:',
        default = 0,
        )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ('-create_at', )