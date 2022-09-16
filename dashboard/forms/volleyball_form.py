from socket import fromshare
from django import forms
from ..models import volleyballModel
from django.db import models
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit

class volleyballForm(forms.ModelForm):
    
    class Meta:
        model=volleyballModel

        fields=[
            "nameoftournament",
            "criteriaofage",
            "gender",
            "dept",
            
        ]