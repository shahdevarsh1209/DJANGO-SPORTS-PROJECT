from socket import fromshare
from django import forms
from ..models import membershipModel
from django.db import models
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit

class membershipForm(forms.ModelForm):
    
    class Meta:
        model=membershipModel

        fields=[
            "FirstName",
            "LastName",
            "Email",
            "PhoneNumber",
            "Address",
        ]