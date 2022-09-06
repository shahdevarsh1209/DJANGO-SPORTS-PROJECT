from django.shortcuts import get_object_or_404,render,redirect
from ..models import evalutionModel
from django.shortcuts import render

from ..forms.evalution_form import evalutionForm


def viewevalution(request):
    context={}
    context["evalutions"]=evalutionModel.objects.all()
    return render(request, "evalution/view.html",context)

def addevalution(request):
    context={}
    form=evalutionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewevalution")
    context['form']=form
    return render(request,"evalution/add.html",context)

def updateevalution(request,id):
    context={}
    obj=get_object_or_404(evalutionModel,id=id)
    form=evalutionForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewevalution")
    context["form"]=form
    return render(request,"evalution/edit.html",context)

def deleteevalution(request,id):
    context={}
    obj=get_object_or_404(evalutionModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewevalution")
    return render(request,"evalution/view.html",context)