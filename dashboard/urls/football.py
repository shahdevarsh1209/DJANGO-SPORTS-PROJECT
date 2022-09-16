from django.urls import path
from ..views.football import *
footballURL=[
    path('viewfootball/',viewfootball,name="viewfootball"),
    path('addfootball/',addfootball,name="addfootball"),  
    path('updatefootball/<id>',updatefootball,name="updatefootball"), 
    path('deletefootball/<id>',deletefootball,name="deletefootball"),
    
]
