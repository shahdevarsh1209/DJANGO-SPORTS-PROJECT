from django.urls import path
from ..views.inquiry import *
inquiryURL=[
    path('viewinquiry/',viewinquiry,name="viewinquiry"),
    path('addinquiry',addinquiry,name="addinquiry"),  
    path('updateinquiry/<id>',updateinquiry,name="updateinquiry"), 
    path('deleteinquiry/<id>',deleteinquiry,name="deleteinquiry"), 
]
