from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from ..models import UserModel

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=UserModel
        fields=('username')