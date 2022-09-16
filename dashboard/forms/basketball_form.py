from socket import fromshare
from django import forms
from ..models import basketballModel
from django.db import models
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit

class basketballForm(forms.ModelForm):
    
    class Meta:
        model=basketballModel

        fields=[
            "nameoftournament",
            "criteriaofage",
            "gender",
            "dept",
        
            
        ]