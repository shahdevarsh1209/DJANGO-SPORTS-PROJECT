from socket import fromshare
from django import forms
from usersite.models import evaluationuserModel
from django.db import models
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit

class evaluationuserForm(forms.ModelForm):
    
    class Meta:
        model=evaluationuserModel

        fields=[
            "firstname",
            "lastname",
            "year",
            "teamname",
            "cfn",
            "cln",  
        ]