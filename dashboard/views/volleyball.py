from django.shortcuts import get_object_or_404,render,redirect
from ..models import volleyballModel
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from ..forms.volleyball_form import volleyballForm
import csv

def viewvolleyball(request):
    context={}
    context["volleyballs"]=volleyballModel.objects.all()
    return render(request, "volleyball/view.html",context)

def addvolleyball(request):
    context={}
    form=volleyballForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.INFO,'Successfully Created')
        return redirect( "viewvolleyball")
    context['form']=form
    return render(request,"volleyball/add.html",context)

def updatevolleyball(request,id):
    context={}
    obj=get_object_or_404(volleyballModel,id=id)
    form=volleyballForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewvolleyball")
    context["form"]=form
    return render(request,"volleyball/edit.html",context)

def deletevolleyball(request,id):
    context={}
    obj=get_object_or_404(volleyballModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewvolleyball")
    return render(request,"volleyball/view.html",context)

def download_volleyballcsv(request):
    response =HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=volleyballtournamentdetails.csv'
    writer = csv.writer(response)
    writer.writerow(['nameoftournament','criteriaofage','gender','dept'])
    for data in volleyballModel.objects.all():
        writer.writerow([data.nameoftournament,data.criteriaofage,data.gender,data.dept]) 

    return response