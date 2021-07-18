from django import forms
from apps.hotels.models import *
from django.forms import ModelForm


class HotelForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', ]

class HotelImageForm(forms.ModelForm):
    class Meta:
        model = MovieImage
        fields = ['image', ]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }