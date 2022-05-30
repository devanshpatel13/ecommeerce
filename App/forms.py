from .models import *
from django import forms
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm



class Customerform(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ["users","username","email","contact","password1","password2"]

    def clean(self):
        cleanned_date = super().clean()
        start = cleanned_date.get('password1')
        end = cleanned_date.get('password2')
        if end != start:
            raise forms.ValidationError('enter qwertyuyt')


class loginform(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields =["username","password"]


class Shopownerform(forms.ModelForm):
    class Meta:
        model = Shopowner
        fields = '__all__'


class addressform(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["first_name", "last_name", "address", "pincode", "city", "state"]
