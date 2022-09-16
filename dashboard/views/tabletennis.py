from django.shortcuts import get_object_or_404,render,redirect
from ..models import tabletennisModel
from django.shortcuts import render

from ..forms.tabletennis_form import tabletennisForm


def viewtt(request):
    context={}
    context["tts"]=tabletennisModel.objects.all()
    return render(request, "tabletennis/view.html",context)

def addtt(request):
    context={}
    form=tabletennisForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewtt")
    context['form']=form
    return render(request,"tabletennis/add.html",context)

def updatett(request,id):
    context={}
    obj=get_object_or_404(tabletennisModel,id=id)
    form=tabletennisForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewtt")
    context["form"]=form
    return render(request,"tabletennis/edit.html",context)

def deletett(request,id):
    context={}
    obj=get_object_or_404(tabletennisModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewtt")
    return render(request,"tabletennis/view.html",context)