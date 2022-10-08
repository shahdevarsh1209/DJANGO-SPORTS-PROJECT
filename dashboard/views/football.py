from django.shortcuts import get_object_or_404,render,redirect
from ..models import footballModel
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from ..forms.football_form import footballForm
import csv

def viewfootball(request):
    context={}
    context["footballs"]=footballModel.objects.all()
    return render(request, "football/view.html",context)

def addfootball(request):
    context={}
    form=footballForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.INFO,'Successfully Created')
        return redirect( "viewfootball")
    context['form']=form
    return render(request,"football/add.html",context)

def updatefootball(request,id):
    context={}
    obj=get_object_or_404(footballModel,id=id)
    form=footballForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewfootball")
    context["form"]=form
    return render(request,"football/edit.html",context)

def deletefootball(request,id):
    context={}
    obj=get_object_or_404(footballModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewfootball")
    return render(request,"football/view.html",context)

def download_footballcsv(request):
    response =HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=footballtournamentdetails.csv'
    writer = csv.writer(response)
    writer.writerow(['nameoftournament','criteriaofage','gender','dept'])
    for data in footballModel.objects.all():
        writer.writerow([data.nameoftournament,data.criteriaofage,data.gender,data.dept]) 

    return response