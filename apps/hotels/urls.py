from django.urls import path
from apps.hotels.views import *


urlpatterns = [
    path('', index, name='index'),
    path('hotel/<int:id>/', detail_hotel, name='detail'),
    path('create/', create_hotel, name='create'),
    path('update/<int:id>/', update_hotel, name='update'),
    path('delete/<int:id>/', delete_hotel, name='delete'),
]