from django.shortcuts import get_object_or_404,render,redirect
from ..models import cricketModel
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from ..forms.cricket_form import cricketForm
import csv

def viewcricket(request):
    context={}
    context["crickets"]=cricketModel.objects.all()
    return render(request, "cricket/view.html",context)

def addcricket(request):
    context={}
    form=cricketForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.INFO,'Successfully Created')
        return redirect( "viewcricket")
    context['form']=form
    return render(request,"cricket/add.html",context)

def updatecricket(request,id):
    context={}
    obj=get_object_or_404(cricketModel,id=id)
    form=cricketForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewcricket")
    context["form"]=form
    return render(request,"cricket/edit.html",context)

def deletecricket(request,id):
    context={}
    obj=get_object_or_404(cricketModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewcricket")
    return render(request,"cricket/view.html",context)

def download_cricketcsv(request):
    response =HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=crickettournamentdetails.csv'
    writer = csv.writer(response)
    writer.writerow(['nameoftournament','criteriaofage','gender','dept','ground'])
    for data in cricketModel.objects.all():
        writer.writerow([data.nameoftournament,data.criteriaofage,data.gender,data.dept,data.ground]) 

    return response