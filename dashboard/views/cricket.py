from django.shortcuts import get_object_or_404,render,redirect
from ..models import cricketModel
from django.shortcuts import render

from ..forms.cricket_form import cricketForm


def viewcricket(request):
    context={}
    context["crickets"]=cricketModel.objects.all()
    return render(request, "cricket/view.html",context)

def addcricket(request):
    context={}
    form=cricketForm(request.POST or None)
    if form.is_valid():
        form.save()
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