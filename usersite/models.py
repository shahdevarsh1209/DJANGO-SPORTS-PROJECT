from django.db import models

# Create your models here.

class inquiryuserModel(models.Model):
    First_Name=models.CharField(max_length=200)
    Last_Name=models.CharField(max_length=200)
    Email=models.CharField(max_length=200)
    Number=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)

class contactuserModel(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.CharField(max_length=200)
    Subject=models.CharField(max_length=200)
    Number=models.IntegerField()
    WriteSomething=models.CharField(max_length=200)