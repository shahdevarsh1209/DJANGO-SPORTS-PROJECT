from django.urls import path
from ..views.message import *
messageURL=[
    path('viewmessage/',viewmessage,name="viewmessage"),
    path('addmessage/',addmessage,name="addmessage"),  
    path('updatemessage/<id>',updatemessage,name="updatemessage"), 
    path('deletemessage/<id>',deletemessage,name="deletemessage"),
    
]
