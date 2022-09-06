from socket import fromshare
from django import forms
from ..models import evalutionModel
from django.db import models
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit

class evalutionForm(forms.ModelForm):
    
    class Meta:
        model=evalutionModel

        fields=[
            "FirstName",
            "LastName",
            "Gender",
            "Year",
            "TeamName",
            "CoachFirstName",
            "CoachLastName",
        ]