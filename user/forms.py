from django import forms
from django.contrib.auth.forms import UserCreationForm

class MyForm(UserCreationForm):
    email = forms.EmailField(max_length=50)