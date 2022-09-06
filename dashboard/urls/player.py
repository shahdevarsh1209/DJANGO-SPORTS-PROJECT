from django.urls import path
from ..views.player import *
playerURL=[
    path('viewplayer/',viewplayer,name="viewplayer"),
    path('addplayer',addplayer,name="addplayer"),  
    path('updateplayer/<id>',updateplayer,name="updateplayer"), 
    path('deleteplayer/<id>',deleteplayer,name="deleteplayer"), 
]
