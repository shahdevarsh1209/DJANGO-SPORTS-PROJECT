from django.urls import path
from ..views.cricket import *
cricketURL=[
    path('viewcricket/',viewcricket,name="viewcricket"),
    path('addcricket/',addcricket,name="addcricket"),  
    path('updatecricket/<id>',updatecricket,name="updatecricket"), 
    path('deletecricket/<id>',deletecricket,name="deletecricket"),
    path('download_cricketcsv',download_cricketcsv,name='download_cricketcsv'),
    
]
