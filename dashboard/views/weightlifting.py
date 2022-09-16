from django.shortcuts import get_object_or_404,render,redirect
from ..models import weightliftingModel
from django.shortcuts import render

from ..forms.weightlifting_form import weightliftingForm


def viewwl(request):
    context={}
    context["wls"]=weightliftingModel.objects.all()
    return render(request, "weightlifting/view.html",context)

def addwl(request):
    context={}
    form=weightliftingForm(request.POST or None)
    if form.is_valid():
        form.save()
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