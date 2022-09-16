from django.urls import path
from ..views.roomservice import *
roomserviceURL=[
    path('viewroomservice/',viewroomservice,name="viewroomservice"),
    path('addroomservice/',addroomservice,name="addroomservice"),  
    path('updateroomservice/<id>',updateroomservice,name="updateroomservice"), 
    path('deleteroomservice/<id>',deleteroomservice,name="deleteroomservice"),
    
]
