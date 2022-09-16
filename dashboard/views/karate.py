from django.shortcuts import get_object_or_404,render,redirect
from ..models import karateModel
from django.shortcuts import render

from ..forms.karate_form import karateForm


def viewkarate(request):
    context={}
    context["karates"]=karateModel.objects.all()
    return render(request, "karate/view.html",context)

def addkarate(request):
    context={}
    form=karateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewkarate")
    context['form']=form
    return render(request,"karate/add.html",context)

def updatekarate(request,id):
    context={}
    obj=get_object_or_404(karateModel,id=id)
    form=karateForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewkarate")
    context["form"]=form
    return render(request,"karate/edit.html",context)

def deletekarate(request,id):
    context={}
    obj=get_object_or_404(karateModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewkarate")
    return render(request,"karate/view.html",context)