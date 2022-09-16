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

type = (
    ('Male','Male'),
    ('Female','Female')
)
sports = (
    ('Cricket','Cricket'),
    ('Volleyball','Volleyball'),
    ('Football','Football'),
    ('Basketball','Basketball'),
    ('Badminton','Badminton')
)
dept = (
    ('LJMCA','LJMCA'),
    ('LJMBA','LJMBA')
)

room = (
    ('SUPER_DELUXE','SUPER_DELUXE'),
    ('SEMI_SUITE','SEMI_SUITE'),
    ('EXECUTIVE_DELXUE','EXECUTIVE_DELXUE'),
    ('SUITE_ROOM','SUITE_ROOM')
)

message = (
    ('Members','Members'),
    ('Childrens','Childrens'),
    ('Adults','Adults')
)

age = (
    ('UNDER_19','UNDER_19'),
    ('UNDER_13','UNDER_13'),
    ('UNDER_21','UNDER_21')
)

tournament = (
    ('REDBULL_CUP','REDBULL_CUP'),
    ('DULEEP_TROPHY','DULEEP_TROPHY'),
    ('RANJI_TROPHY','RANJI_TROPHY'),
    ('VIJAY_HAZARE','VIJAY_HAZARE'),
    ('IPL','IPL')

)

ground = (
    ('NAREDRA_MODI_GROUND','NAREDRA_MODI_GROUND'),
    ('C_B_PATEL_INTERNATION_CRICKET_GROUND','C_B_PATEL_INTERNATION_CRICKET_GROUND'),
    ('GUJARAT_COLLEGE_GROUND','GUJARAT_COLLEGE_GROUND')
)

football =(
    ('DURAND_CUP','DURAND_CUP'),
    ('IFA_SHIELD','IFA_SHIELD'),
    ('SUBROTO_CLUB','SUBROTO_CLUB'),
    ('SANTOSH_TROPHY','SANTOSH_TROPHY'),
    ('ISL','ISL')
)

basketball = (
    ('ASIAN_CHAMPIONSHIPS','ASIAN_CHAMPIONSHIPS'),
    ('AFRICAN_CHAMPIONSHIPS','AFRICAN_CHAMPIONSHIPS'),
    ('EUROPEAN_CHAMPIONSHIPS','EUROPEAN_CHAMPIONSHIPS')
)

karate = (
    ('SPORT_KARATE_INTERNATIONAL','SPORT_KARATE_INTERNATIONAL'),
    ('NATIONAL_BLACK_BELT_LEAGUE','NATIONAL_BLACK_BELT_LEAGUE'),
    ('PROFESSIONAL_POINT_KARATE_FEDERAATION','PROFESSIONAL_POINT_KARATE_FEDERAATION'),
    ('UNIVERSAL_MARTIAL_ARTS_ASSOCIATE','UNIVERSAL_MARTIAL_ARTS_ASSOCIATE'),
    ('NORTH_AMERICA_SPORT_KARATE_ASSOCIATION','NORTH_AMERICA_SPORT_KARATE_ASSOCIATION')
)

tt = (
    ('TABLE_TENNIS_TOURS_AND_SERIES','TABLE_TENNIS_TOURS_AND_SERIES'),
    ('ASIAN_JUNIOR AND_CADET_TABLE_TENNIS_CHAMPIONSHIPS','ASIAN_JUNIOR AND_CADET_TABLE_TENNIS_CHAMPIONSHIPS'),
    ('HUNGRIAN_OPEN','HUNGRIAN_OPEN'),
    ('ITTP','ITTP'),
    ('PAN_AMERICAN_TABLE_TENNIS_CUP','PAN_AMERICAN_TABLE_TENNIS_CUP')
)

wl = (
    ('WORLD_WEIGHTLIFTING_CHAMPIONSHIP','WORLD_WEIGHTLIFTING_CHAMPIONSHIP'),
    ('INTERNATIONAL_WEIGHTLIFTING_FEDERATION','INTERNATIONAL_WEIGHTLIFTING_FEDERATION'),
    ('IWLF_YOUNG_NATION_WEIGHTLIFTING_CHAMPIONSHIP','IWLF_YOUNG_NATION_WEIGHTLIFTING_CHAMPIONSHIP'),
    ('IWLF_JUNIOR_NATION_WEIGHTLIFTING_CHAMPIONSHIP','IWLF_JUNIOR_NATION_WEIGHTLIFTING_CHAMPIONSHIP'),
    ('COMMONWEALTH_GAMES','COMMONWEALTH_GAMES')
)

volleyball = (
    ('FEDERATION_CUP','FEDERATION_CUP'),
    ('NATIONAL_VOLLEYBALL_CHAMPIONSHIP','NATIONAL_VOLLEYBALL_CHAMPIONSHIP'),
    ('BEACH_VOLLEYBALL','BEACH_VOLLEYBALL'),
    ('PRO_VOLLEYBALL_LEAGUE','PRO_VOLLEYBALL_LEAGUE'),
    ('SUB_JUNIOR_NATIONAL_VOLLEYBALL_CHAMPIONSHIP','SUB_JUNIOR_NATIONAL_VOLLEYBALL_CHAMPIONSHIP')
)
class UserModel(AbstractUser):

    userProfile=models.ImageField(upload_to="userProfile")
    #type = models.CharField(max_length=200,choices=type,default='user')

class CategoryModel(models.Model):
    title=models.CharField(max_length=200)  
    description= models.TextField()

class playerModel(models.Model):
    Name=models.CharField(max_length=200)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=6,choices=type,default='Male')
    SportsName=models.CharField(max_length=50,choices=sports,default='cricket')
    ContactNumber=models.IntegerField()

class tournamentModel(models.Model):
    Name=models.CharField(max_length=200)
    SportsName=models.CharField(max_length=50,choices=sports,default='cricket')
    DOB=models.DateField()
    Dept=models.CharField(max_length=50,choices=dept,default='LJMCA')
    Achivement=models.CharField(max_length=200)

class membershipModel(models.Model):
    FirstName=models.CharField(max_length=200)
    LastName=models.CharField(max_length=200)
    Email=models.CharField(max_length=200,blank = False,null = False)
    PhoneNumber=models.IntegerField()
    Address=models.TextField()

class inquiryModel(models.Model):
    Name=models.CharField(max_length=200)
    Gender=models.CharField(max_length=6,choices=type,default='Male')
    School=models.CharField(max_length=200)
    ParentsName =models.CharField(max_length=200)
    Email=models.CharField(max_length=200)
    PlayedTournament=models.CharField(max_length=200)

class evalutionModel(models.Model):
    FirstName=models.CharField(max_length=200)
    LastName=models.CharField(max_length=200)
    Gender=models.CharField(max_length=6,choices=type,default='Male')
    Year=models.CharField(max_length=4)
    TeamName=models.CharField(max_length=50)
    CoachFirstName=models.CharField(max_length=200) 
    CoachLastName=models.CharField(max_length=200)

class roomserviceModel(models.Model):
    category=models.CharField(max_length=200,choices=room,default='SUPER_DELUXE')
    price=models.IntegerField()

class messageModel(models.Model):
    category=models.CharField(max_length=200,choices=message,default='Members')
    message=models.CharField(max_length=200)

class cricketModel(models.Model):
    nameoftournament=models.CharField(max_length=200,choices=tournament,default='REDBULL_CUP')
    criteriaofage=models.CharField(max_length=200,choices=age,default='UNDER_19')
    gender=models.CharField(max_length=6,choices=type,default='Male')
    dept=models.CharField(max_length=50,choices=dept,default='LJMCA')
    ground=models.CharField(max_length=50,choices=ground,default='NAREDRA_MODI_GROUND')
     
class footballModel(models.Model):
    nameoftournament=models.CharField(max_length=200,choices=football,default='ISL')
    criteriaofage=models.CharField(max_length=200,choices=age,default='UNDER_19')
    gender=models.CharField(max_length=6,choices=type,default='Male')
    dept=models.CharField(max_length=50,choices=dept,default='LJMCA')   

class basketballModel(models.Model):
    nameoftournament=models.CharField(max_length=200,choices=basketball,default='ASIAN_CHAMPIONSHIPS')
    criteriaofage=models.CharField(max_length=200,choices=age,default='UNDER_19')
    gender=models.CharField(max_length=6,choices=type,default='Male')
    dept=models.CharField(max_length=50,choices=dept,default='LJMCA')           
           
class karateModel(models.Model):
    nameoftournament=models.CharField(max_length=200,choices=karate,default='ASIAN_CHAMPIONSHIPS')
    criteriaofage=models.CharField(max_length=200,choices=age,default='UNDER_19')
    gender=models.CharField(max_length=6,choices=type,default='Male')
    dept=models.CharField(max_length=50,choices=dept,default='LJMCA')

class tabletennisModel(models.Model):
    nameoftournament=models.CharField(max_length=200,choices=tt,default='HUNGRIAN_OPEN')
    criteriaofage=models.CharField(max_length=200,choices=age,default='UNDER_19')
    gender=models.CharField(max_length=6,choices=type,default='Male')
    dept=models.CharField(max_length=50,choices=dept,default='LJMCA')

class weightliftingModel(models.Model):
    nameoftournament=models.CharField(max_length=200,choices=wl,default='WORLD_WEIGHTLIFTING_CHAMPIONSHIP')
    criteriaofage=models.CharField(max_length=200,choices=age,default='UNDER_19')
    gender=models.CharField(max_length=6,choices=type,default='Male')
    dept=models.CharField(max_length=50,choices=dept,default='LJMCA')

class volleyballModel(models.Model):
    nameoftournament=models.CharField(max_length=200,choices=volleyball,default='FEDERATION_CUP')
    criteriaofage=models.CharField(max_length=200,choices=age,default='UNDER_19')
    gender=models.CharField(max_length=6,choices=type,default='Male')
    dept=models.CharField(max_length=50,choices=dept,default='LJMCA')

