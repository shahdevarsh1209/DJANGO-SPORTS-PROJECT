from django.urls import path
from ..views.volleyball import *
volleyballURL=[
    path('viewvolleyball/',viewvolleyball,name="viewvolleyball"),
    path('addvolleyball/',addvolleyball,name="addvolleyball"),  
    path('updatevolleyball/<id>',updatevolleyball,name="updatevolleyball"), 
    path('deletevolleyball/<id>',deletevolleyball,name="deletevolleyball"),
    
]
