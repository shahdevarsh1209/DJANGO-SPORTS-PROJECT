from socket import fromshare
from django import forms
from ..models import messageModel
from django.db import models
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit

class messageForm(forms.ModelForm):
    
    class Meta:
        model=messageModel

        fields=[
            "category",
            "message",
            
        ]