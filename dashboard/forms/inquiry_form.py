from socket import fromshare
from django import forms
from ..models import inquiryModel
from django.db import models
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit

class inquiryForm(forms.ModelForm):
    
    class Meta:
        model=inquiryModel

        fields=[
            "Name",
            "Gender",
            "School",
            "ParentsName",
            "Email",
            "PlayedTournament",
        ]