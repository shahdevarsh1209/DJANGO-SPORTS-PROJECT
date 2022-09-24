from django.urls import path
from ..views.karate import *
karateURL=[
    path('viewkarate/',viewkarate,name="viewkarate"),
    path('addkarate/',addkarate,name="addkarate"),  
    path('updatekarate/<id>',updatekarate,name="updatekarate"), 
    path('deletekarate/<id>',deletekarate,name="deletekarate"),
    path('download_karatecsv',download_karatecsv,name='download_karatecsv'),

]
