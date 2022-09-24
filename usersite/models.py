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

class evaluationuserModel(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    year=models.IntegerField()
    teamname=models.CharField(max_length=200)
    cfn=models.CharField(max_length=200)
    cln=models.CharField(max_length=200)

class tournamentuserModel(models.Model):
    firstname=models.CharField(max_length=200)
    sportsname=models.CharField(max_length=200)
    dob=models.IntegerField()
    dept=models.CharField(max_length=200)
    achivement=models.CharField(max_length=200)

class feedbackuserModel(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    number=models.IntegerField()
    subject=models.CharField(max_length=200)
    write=models.CharField(max_length=200)
    