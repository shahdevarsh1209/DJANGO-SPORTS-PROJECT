from django.urls import path
from ..views.category import *
categoryURL=[
    path('viewCategory/',viewCategory,name="viewCategory"),
    path('addCategory/',addCategory,name="addCategory"),  
    path('updateCatrogry/<id>',updateCategory,name="updateCategory"), 
    path('deleteCategory/<id>',deleteCategory,name="deleteCategory"),
    path('bulkUpload/',bulk_upload,name="bulkUpload"),
    path('upload_csv',upload_csv,name='upload_csv'),
    path('download_csv',download_csv,name='download_csv'),

]
