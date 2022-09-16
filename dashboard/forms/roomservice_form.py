from socket import fromshare
from django import forms
from ..models import roomserviceModel
from django.db import models
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit

class roomserviceForm(forms.ModelForm):
    
    class Meta:
        model=roomserviceModel

        fields=[
            "category",
            "price",
        ]