from django.shortcuts import render, redirect
from apps.orders.models import *
from apps.orders.forms import OrderForm
from django.forms import inlineformset_factory
# Create your views here.


def order_index(request):
    orders = Hotel.objects.all() 
    return render(request, 'order/index.html', {'orders': orders})   
