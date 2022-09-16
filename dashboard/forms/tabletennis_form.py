from socket import fromshare
from django import forms
from ..models import tabletennisModel
from django.db import models
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit

class tabletennisForm(forms.ModelForm):
    
    class Meta:
        model=tabletennisModel

        fields=[
            "nameoftournament",
            "criteriaofage",
            "gender",
            "dept",
            
        ]