from socket import fromshare
from django import forms
from usersite.models import inquiryuserModel
from django.db import models
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit

class inquiryuserForm(forms.ModelForm):
    
    class Meta:
        model=inquiryuserModel

        fields=[
            "First_Name",
            "Last_Name",
            "Email",
            "Number",
            "Address",
            
        ]