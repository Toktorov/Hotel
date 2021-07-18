from django.shortcuts import render
from apps.hotels.models import *

# Create your views here.
def index(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel/index.html', {'hotels': hotels})

def detail(request, id=id):
    hotels = Hotel.objects.get(id=id)
    return render(request, 'hotel/detail.html', {"hotel": hotels})