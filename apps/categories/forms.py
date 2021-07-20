from django import forms
from apps.categories.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'parent']
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'parent': forms.Select(attrs={'class': "form-control"}),
        }