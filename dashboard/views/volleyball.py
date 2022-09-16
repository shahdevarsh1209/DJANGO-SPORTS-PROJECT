from django.shortcuts import get_object_or_404,render,redirect
from ..models import volleyballModel
from django.shortcuts import render

from ..forms.volleyball_form import volleyballForm


def viewvolleyball(request):
    context={}
    context["volleyballs"]=volleyballModel.objects.all()
    return render(request, "volleyball/view.html",context)

def addvolleyball(request):
    context={}
    form=volleyballForm(request.POST or None)
    if form.is_valid():
        form.save()
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