from socket import fromshare
from django import forms
from usersite.models import tournamentuserModel
from django.db import models
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit

class tournamentuserForm(forms.ModelForm):
    
    class Meta:
        model=tournamentuserModel

        fields=[
            "firstname",
            "sportsname",
            "dob",
            "dept",
            "achivement",
  
        ]