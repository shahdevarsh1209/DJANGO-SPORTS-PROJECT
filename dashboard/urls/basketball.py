from django.urls import path
from ..views.basketball import *
basketballURL=[
    path('viewbasketball/',viewbasketball,name="viewbasketball"),
    path('addbasketball/',addbasketball,name="addbasketball"),  
    path('updatebasketball/<id>',updatebasketball,name="updatebasketball"), 
    path('deletebasketball/<id>',deletebasketball,name="deletebasketball"),
    path('download_basketballcsv',download_basketballcsv,name='download_basketballcsv'),
]
