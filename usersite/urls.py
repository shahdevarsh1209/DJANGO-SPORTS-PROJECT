from django.contrib import admin 
from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.homepage,name="homepage"),
    path('blog/',views.blog,name="blog"),
    path('contact/',views.contact,name="contact"),
    path('evaluation/',views.evaluation,name="evaluation"),
    path('feedback/',views.feedback,name="feedback"),
    path('inquiry/',views.inquiry,name="inquiry"),
    path('inquiryuser/',views.inquiryuser,name="inquiryuser"),
    path('main/',views.main,name="main"),
    path('matches/',views.matches,name="matches"),
    path('players/',views.players,name="players"),
    path('single/',views.single,name="single"),
    path('tournament/',views.tournament,name="tournament"),
    path('cricket/',views.cricket,name="cricket"),
]
