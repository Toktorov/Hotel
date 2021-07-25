from django.shortcuts import render, redirect, get_object_or_404
from apps.hotels.models import *
from apps.hotels.forms import HotelForm, HotelImageForm
from django.forms import inlineformset_factory

# Create your views here.
def index(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel/index.html', {'hotels': hotels})

def detail_hotel(request, id=id):
    hotels = Hotel.objects.get(id=id)
    if 'like' in request.POST:
        try:
            like = Like.objects.get(user=request.user, hotels=hotels)
            like.delete()
        except:
            Like.objects.create(user=request.user, hotels=hotels)
    
    if 'comment' in request.POST:
            try:
                text = request.POST.get('text')
                comment_obj = Comment.objects.create(user=request.user, hotels=hotels, text=text)
                return redirect('detail', hotel.id)
            except:
                print("Error")
    return render(request, 'hotel/detail.html', {"hotel": hotels})

def create_hotel(request):
    form = HotelForm(request.POST or None)
    HotelImageFormSet = inlineformset_factory(Hotel, HotelImage, form=HotelImageForm, extra=1)
    if request.method == 'POST':
        if form.is_valid():
            hotel = Hotel()
            hotel.user = request.user
            hotel.title = form.cleaned_data['title']
            hotel.description = form.cleaned_data['description']
            hotel.price = form.cleaned_data['price']
            hotel.category = form.cleaned_data['category']
            hotel.wifi = form.cleaned_data['wifi']
            hotel.parking = form.cleaned_data['parking']
            hotel.save()
            formset = HotelImageFormSet(request.POST, request.FILES, instance=hotel)
            if formset.is_valid():
                formset.save()
            return redirect('index')
    formset = HotelImageFormSet()
    return render(request, 'hotel/create.html', locals())

def update_hotel(request, id):
    hotel = get_object_or_404(Hotel, id=id)
    form = HotelForm(request.POST, None, instance=hotel)
    HotelImageFormset = inlineformset_factory(Hotel, HotelImage, form=HotelImageForm, extra=1)
    if form.is_valid():
        hotel = form.save()
        formset = HotelImageFormset(request.POST, request.FILES, instance=hotel)
        if formset.is_valid():
            formset.save()
        return redirect('index')
    formset = HotelImageFormset(instance=hotel)
    return render(request, 'hotel/update.html', locals())

def delete_hotel(request, id):
    if request.method == 'POST':
        hotel = Hotel.objects.get(id=id)
        hotel.delete()
        return redirect('index')
    return render(request, 'hotel/delete.html')