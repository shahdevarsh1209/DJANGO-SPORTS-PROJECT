from socket import fromshare
from django import forms
from ..models import tournamentModel
from django.db import models
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit

class tournamentForm(forms.ModelForm):
    
    class Meta:
        model=tournamentModel

        fields=[
            "Name",
            "SportsName",
            "DOB",
            "Dept",
            "Achivement",
        ]