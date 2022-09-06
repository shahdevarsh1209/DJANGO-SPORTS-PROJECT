from django.urls import path
from ..views.category import *
categoryURL=[
    path('viewCategory/',viewCategory,name="viewCategory"),
    path('addCategory/',addCategory,name="addCategory"),  
    path('updateCatrogry/<id>',updateCategory,name="updateCategory"), 
    path('deleteCategory/<id>',deleteCategory,name="deleteCategory"), 
]
