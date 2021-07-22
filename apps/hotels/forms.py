from django import forms
from apps.hotels.models import *
from django.forms import ModelForm


class HotelForm(ModelForm):
    class Meta:
        model = Hotel
        exclude = []
        fields = ['title', 'description', 'price', 'category', 'wifi', 'parking', ]
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'wifi': forms.TextInput(attrs={'class': "form-control"}),
            'parking': forms.TextInput(attrs={'class': "form-control"}),
        }

class HotelImageForm(forms.ModelForm):
    class Meta:
        model = HotelImage
        fields = ['image', ]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
