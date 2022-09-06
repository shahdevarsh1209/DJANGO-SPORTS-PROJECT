from ast import Index
from django.urls import path
from ..views import *
from django.contrib.auth import views as auth_views
authUrls=[
    path('index', index,name='index'),
        path('register/',SignUp.as_view(),name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]