from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name',  'price','description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter product price'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter product description'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','email', 'password1', 'password2']
        