from django.shortcuts import get_object_or_404,render,redirect
from ..models import weightliftingModel
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from ..forms.weightlifting_form import weightliftingForm
import csv

def viewwl(request):
    context={}
    context["wls"]=weightliftingModel.objects.all()
    return render(request, "weightlifting/view.html",context)

def addwl(request):
    context={}
    form=weightliftingForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.INFO,'Successfully Created')
        return redirect( "viewwl")
    context['form']=form
    return render(request,"weightlifting/add.html",context)

def updatewl(request,id):
    context={}
    obj=get_object_or_404(weightliftingModel,id=id)
    form=weightliftingForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewwl")
    context["form"]=form
    return render(request,"weightlifting/edit.html",context)

def deletewl(request,id):
    context={}
    obj=get_object_or_404(weightliftingModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewwl")
    return render(request,"weightlifting/view.html",context)

def download_wlcsv(request):
    response =HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=weightliftingtournamentdetails.csv'
    writer = csv.writer(response)
    writer.writerow(['nameoftournament','criteriaofage','gender','dept'])
    for data in weightliftingModel.objects.all():
        writer.writerow([data.nameoftournament,data.criteriaofage,data.gender,data.dept]) 

    return response