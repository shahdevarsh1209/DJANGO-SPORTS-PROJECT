from django.shortcuts import get_object_or_404,render,redirect
from ..models import basketballModel
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from ..forms.basketball_form import basketballForm
import csv

def viewbasketball(request):
    context={}
    context["basketballs"]=basketballModel.objects.all()
    return render(request, "basketball/view.html",context)

def addbasketball(request):
    context={}
    form=basketballForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.INFO,'Successfully Created')
        return redirect( "viewbasketball")
    context['form']=form
    return render(request,"basketball/add.html",context)

def updatebasketball(request,id):
    context={}
    obj=get_object_or_404(basketballModel,id=id)
    form=basketballForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewbasketball")
    context["form"]=form
    return render(request,"basketball/edit.html",context)

def deletebasketball(request,id):
    context={}
    obj=get_object_or_404(basketballModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewbasketball")
    return render(request,"basketball/view.html",context)

def download_basketballcsv(request):
    response =HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=basketballtournamentdetails.csv'
    writer = csv.writer(response)
    writer.writerow(['nameoftournament','criteriaofage','gender','dept'])
    for data in basketballModel.objects.all():
        writer.writerow([data.nameoftournament,data.criteriaofage,data.gender,data.dept]) 

    return response