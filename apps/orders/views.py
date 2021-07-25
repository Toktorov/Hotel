from django.shortcuts import render, redirect
from apps.orders.models import *
from apps.orders.forms import OrderForm
from django.forms import inlineformset_factory
from django.views.generic import ListView, DetailView
# Create your views here.


class OrderIndexView(ListView):
    model = Order
    template_name = 'order/index.html'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/detail.html'

def create_order(request):
    form = OrderForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            hotel = Hotel()
            hotel.user = request.user
            hotel.name = form.cleaned_data['name']
            hotel.surname = form.cleaned_data['surname']
            hotel.fatherland = form.cleaned_data['fatherland']
            hotel.arrival_date = form.cleaned_data['arrival_date']
            hotel.wifi = form.cleaned_data['departure_date']
            hotel.id_card = form.cleaned_data['id_card']
            hotel.save()
            return redirect('order_index')
    return render(request, 'order/create.html', locals())
