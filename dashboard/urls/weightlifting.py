from django.urls import path
from ..views.weightlifting import *
weightliftingURL=[
    path('viewwl/',viewwl,name="viewwl"),
    path('addwl',addwl,name="addwl"),  
    path('updatewl/<id>',updatewl,name="updatewl"), 
    path('deletewl/<id>',deletewl,name="deletewl"),
    path('download_wlcsv',download_wlcsv,name='download_wlcsv'),
]
