from socket import fromshare
from django import forms
from ..models import cricketModel
from django.db import models
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit

class cricketForm(forms.ModelForm):
    
    class Meta:
        model=cricketModel

        fields=[
            "nameoftournament",
            "criteriaofage",
            "gender",
            "dept",
            "ground",
            
        ]