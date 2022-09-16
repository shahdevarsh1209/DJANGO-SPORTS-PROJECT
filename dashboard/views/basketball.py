from django.shortcuts import get_object_or_404,render,redirect
from ..models import basketballModel
from django.shortcuts import render

from ..forms.basketball_form import basketballForm


def viewbasketball(request):
    context={}
    context["basketballs"]=basketballModel.objects.all()
    return render(request, "basketball/view.html",context)

def addbasketball(request):
    context={}
    form=basketballForm(request.POST or None)
    if form.is_valid():
        form.save()
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