from django.urls import path
from ..views.membership import *
membershipURL=[
    path('viewmembership/',viewmembership,name="viewmembership"),
    path('addmembership',addmembership,name="addmembership"),  
    path('updatemembership/<id>',updatemembership,name="updatemembership"), 
    path('deletemembership/<id>',deletemembership,name="deletemembership"), 
]
