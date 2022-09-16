from django.urls import path
from ..views.tabletennis import *
tabletennisURL=[
    path('viewtt/',viewtt,name="viewtt"),
    path('addtt/',addtt,name="addtt"),  
    path('updatett/<id>',updatett,name="updatett"), 
    path('deletett/<id>',deletett,name="deletett"),
    
]
