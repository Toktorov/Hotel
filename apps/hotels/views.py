from django.shortcuts import render
from apps.hotels.models import *

# Create your views here.
def index(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel/index.html', {'hotels': hotels})
