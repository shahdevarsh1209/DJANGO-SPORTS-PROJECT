from socket import fromshare
from django import forms
from usersite.models import feedbackuserModel
from django.db import models
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit

class feedbackuserForm(forms.ModelForm):
    
    class Meta:
        model=feedbackuserModel

        fields=[
            "name",
            "email",
            "number",
            "subject",
            "write",  
        ]