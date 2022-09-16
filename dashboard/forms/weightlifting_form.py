from socket import fromshare
from django import forms
from ..models import weightliftingModel
from django.db import models
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit

class weightliftingForm(forms.ModelForm):
    
    class Meta:
        model=weightliftingModel

        fields=[
            "nameoftournament",
            "criteriaofage",
            "gender",
            "dept",
            
        ]