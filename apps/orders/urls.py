from django.urls import path
from apps.orders.views import *


urlpatterns = [
    path('', order_index, name = 'order_index'),
]