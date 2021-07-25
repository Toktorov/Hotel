from django import forms
from apps.orders.models import Order
from django.forms import ModelForm

class OrderForm(ModelForm):
    class Meta:
        model = Order 
        fields = ['arrival_date', 'departure_date', 'name', 'surname', 'fatherland', 'id_card']
        widgets = {
            'arrival_date': forms.DateInput(attrs={'class': "form-control"}),
            'departure_date': forms.DateInput(attrs={'class': "form-control"}),
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'surname': forms.TextInput(attrs={'class': "form-control"}),
            'fatherland': forms.TextInput(attrs={'class': "form-control"}),
            'id_card': forms.NumberInput(attrs={'class': 'form-control'}),
        }