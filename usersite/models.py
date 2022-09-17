from django.db import models

# Create your models here.

class inquiryuserModel(models.Model):
    First_Name=models.CharField(max_length=200)
    Last_Name=models.CharField(max_length=200)
    Email=models.CharField(max_length=200)
    Number=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)