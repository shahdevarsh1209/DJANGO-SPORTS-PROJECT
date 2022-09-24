from django.contrib import admin 
from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.homepage,name="homepage"),
    path('blog/',views.blog,name="blog"),
    path('contact/',views.contact,name="contact"),
    path('contactuser/',views.contactuser,name="contactuser"),
    path('evaluation/',views.evaluation,name="evaluation"),
    path('evaluationuser/',views.evaluationuser,name="evaluationuser"),
    path('feedback/',views.feedback,name="feedback"),
    path('feedbackuser/',views.feedbackuser,name="feedbackuser"),
    path('inquiry/',views.inquiry,name="inquiry"),
    path('inquiryuser/',views.inquiryuser,name="inquiryuser"),
    path('main/',views.main,name="main"),
    path('matches/',views.matches,name="matches"),
    path('players/',views.players,name="players"),
    path('single/',views.single,name="single"),
    path('tournament/',views.tournament,name="tournament"),
    path('tournamentuser/',views.tournamentuser,name="tournamentuser"),
    path('cricket/',views.cricket,name="cricket"),
    path('football/',views.football,name="football"),
    path('basketball/',views.basketball,name="basketball"),
    path('volleyball/',views.volleyball,name="volleyball"),
    path('karate/',views.karate,name="karate"),
    path('tabletennis/',views.tabletennis,name="tabletennis"),
    path('weightlifting/',views.weightlifting,name="weightlifting"),
]
