from django.shortcuts import get_object_or_404,render,redirect
from ..models import footballModel
from django.shortcuts import render

from ..forms.football_form import footballForm


def viewfootball(request):
    context={}
    context["footballs"]=footballModel.objects.all()
    return render(request, "football/view.html",context)

def addfootball(request):
    context={}
    form=footballForm(request.POST or None)
    if form.is_valid():
        form.save()
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