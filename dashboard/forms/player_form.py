from socket import fromshare
from django import forms
from ..models import playerModel
from django.db import models
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit

class playerForm(forms.ModelForm):
    
    class Meta:
        model=playerModel

        fields=[
            "Name",
            "Age",
            "Gender",
            "SportsName",
            "ContactNumber",
        ]