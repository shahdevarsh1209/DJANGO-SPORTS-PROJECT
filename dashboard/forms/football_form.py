from socket import fromshare
from django import forms
from ..models import footballModel
from django.db import models
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit

class footballForm(forms.ModelForm):
    
    class Meta:
        model=footballModel

        fields=[
            "nameoftournament",
            "criteriaofage",
            "gender",
            "dept",
            
        ]