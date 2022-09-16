from socket import fromshare
from django import forms
from ..models import karateModel
from django.db import models
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit

class karateForm(forms.ModelForm):
    
    class Meta:
        model=karateModel

        fields=[
            "nameoftournament",
            "criteriaofage",
            "gender",
            "dept",
            
        ]