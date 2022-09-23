from socket import fromshare
from django import forms
from usersite.models import contactuserModel
from django.db import models
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit

class contactuserForm(forms.ModelForm):
    
    class Meta:
        model=contactuserModel

        fields=[
            "Name",
            "Email",
            "Subject",
            "Number",
            "WriteSomething",  
        ]