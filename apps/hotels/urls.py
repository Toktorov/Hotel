from django.urls import path
from apps.hotels.views import *


urlpatterns = [
    path('', index, name='index'),
    path('hotel/<int:id>/', detail, name='detail'),
]