from django.urls import path
from ..views.tournament import *
tournamentURL=[
    path('viewtournament/',viewtournament,name="viewtournament"),
    path('addtournament',addtournament,name="addtournament"),  
    path('updatetournament/<id>',updatetournament,name="updatetournament"), 
    path('deletetournament/<id>',deletetournament,name="deletetournament"), 
]
