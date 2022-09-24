from django.shortcuts import render,redirect
from dashboard.models import *
from usersite.form.inquiryuser_form import inquiryuserForm 
from usersite.form.contactuser_form import contactuserForm 
from usersite.form.evaluationuser_form import evaluationuserForm
from usersite.form.tournamentuser_form import tournamentuserForm
from usersite.form.feedbackuser_form import feedbackuserForm
from usersite.models import *
from django.contrib import messages
#from django.http import HttpResponce

def homepage(request):
    return render(request,'homepage.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def contactuser(request):
    if request.method == "POST":
        form = contactuserForm(request.POST or None)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,"DONE BKA ,DATA SAVE :)")
                return render(request,'contact.html')
            except:
                pass
    else:
        form = contactuserForm()
    return render(request,'contact.html',{'form':form})


def evaluation(request):
    return render(request,'evaluation.html')

def evaluationuser(request):
    if request.method == "POST":
        form = evaluationuserForm(request.POST or None)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,"DONE BKA,DATA SAVE :)")
                return render(request,'evaluation.html')
            except:
                pass
    else:
        form = evaluationuserForm()
    return render(request,'evaluation.html',{'form':form})

def feedback(request):
    return render(request,'feedback.html')

def feedbackuser(request):
    if request.method == "POST":
        form = feedbackuserForm(request.POST or None)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,"DONE BKA ,DATA SAVE :)")
                return render(request,'feedback.html')
            except:
                pass
    else:
        form = feedbackuserForm()
    return render(request,'feedback.html',{'form':form})

def inquiry(request):
    return render(request,'inquiry.html')

def inquiryuser(request):
    if request.method == "POST":
        form = inquiryuserForm(request.POST or None)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,"DONE BKA ,DATA SAVE :)")
                return render(request,'inquiry.html')
            except:
                pass
    else:
        form = inquiryuserForm()
    return render(request,'inquiry.html',{'form':form})


def main(request):
    return render(request,'main.html')

def matches(request):
    return render(request,'matches.html')

def players(request):
    return render(request,'players.html')

def single(request):
    return render(request,'single.html')

def tournament(request):
    return render(request,'tournament.html')

def tournamentuser(request):
    if request.method == "POST":
        form = tournamentuserForm(request.POST or None)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,"DONE BKA ,DATA SAVE :)")
                return render(request,'tournament.html')
            except:
                pass
    else:
        form = tournamentuserForm()
    return render(request,'tournament.html',{'form':form})

def cricket(request):
    context={}
    context["crickets"]=cricketModel.objects.all()
    return render(request,'cricket/cricketview.html',context)

def football(request):
    context={}
    context["footballs"]=footballModel.objects.all()
    return render(request,'football/footballview.html',context)

def basketball(request):
    context={}
    context["basketballs"]=basketballModel.objects.all()
    return render(request,'basketball/basketballview.html',context)

def volleyball(request):
    context={}
    context["volleyballs"]=volleyballModel.objects.all()
    return render(request,'volleyball/volleyballview.html',context)

def karate(request):
    context={}
    context["karates"]=karateModel.objects.all()
    return render(request,'karate/karateview.html',context)

def tabletennis(request):
    context={}
    context["tts"]=tabletennisModel.objects.all()
    return render(request,'tabletennis/tabletennisview.html',context)

def weightlifting(request):
    context={}
    context["wls"]=weightliftingModel.objects.all()
    return render(request,'weightlifting/weightliftingview.html',context)