from django.urls import path
from ..views.evalution import *
evalutionURL=[
    path('viewevalution/',viewevalution,name="viewevalution"),
    path('addevalution',addevalution,name="addevalution"),  
    path('updateevalution/<id>',updateevalution,name="updateevalution"), 
    path('deleteevalution/<id>',deleteevalution,name="deleteevalution"), 
]
