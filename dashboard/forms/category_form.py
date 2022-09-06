from socket import fromshare
from django import forms
from ..models import CategoryModel
from django.db import models
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model=CategoryModel

        fields=[
            "title",
            "description",
        ]