from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class UserForm(UserCreationForm):
    """
    Form that uses built-in UserCreationForm to handle user creation
    """
    first_name = forms.CharField(max_length=30, required=True,
                                 widget=forms.TextInput(attrs={'placeholder': '*Your first name...'}))
    last_name = forms.CharField(max_length=30, required=True,
                                widget=forms.TextInput(attrs={'placeholder': '*Your last name...'}))
    username = forms.EmailField(max_length=254, required=True,
                                widget=forms.TextInput(attrs={'placeholder': '*Email...'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '*Password...', 'class': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '*Confirm Password...',
                                                                  'class': 'password'}))
    # reCAPTCHA token
    token = forms.CharField(widget=forms.HiddenInput())
