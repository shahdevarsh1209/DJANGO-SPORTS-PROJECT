#from django.db import models

# Create your models here.
'''class Position(models.Model):
    title = models.CharField(max_length=30)

class Employee(models.Model):
    fullname = models.CharField(max_length=30)
    emp_code = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    repassword=models.CharField(max_length=30)
'''
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User, Group
# Create your models here.

class UserModel(AbstractUser):
    pass

class CategoryModel(models.Model):
    title=models.CharField(max_length=200)  
    description= models.TextField()

class playerModel(models.Model):
    Name=models.CharField(max_length=200)
    Age=models.IntegerField()
    Gender=models.TextField()
    SportsName=models.TextField()
    ContactNumber=models.IntegerField()

class tournamentModel(models.Model):
    Name=models.CharField(max_length=200)
    SportsName=models.TextField()
    DOB=models.IntegerField()
    Dept=models.TextField()
    Achivement=models.TextField()

class membershipModel(models.Model):
    FirstName=models.TextField()
    LastName=models.TextField()
    Email=models.TextField()
    PhoneNumber=models.TextField()
    Address=models.TextField()

class inquiryModel(models.Model):
    Name=models.TextField()
    Gender=models.TextField()
    School=models.TextField()
    ParentsName =models.TextField()
    Email=models.TextField() 
    PlayedTournament=models.TextField()

class evalutionModel(models.Model):
    FirstName=models.TextField()
    LastName=models.TextField()
    Gender=models.TextField()
    Year=models.TextField()
    TeamName=models.TextField() 
    CoachFirstName=models.TextField() 
    CoachLastName=models.TextField()


