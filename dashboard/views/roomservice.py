from django.shortcuts import get_object_or_404,render,redirect
from ..models import roomserviceModel
from django.shortcuts import render
from django.contrib import messages

from ..forms.roomservice_form import roomserviceForm


def viewroomservice(request):
    context={}
    context["rooms"]=roomserviceModel.objects.all()
    return render(request, "roomservice/view.html",context)

def addroomservice(request):
    context={}
    form=roomserviceForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.INFO,'Successfully Created')
        return redirect( "viewroomservice")
    context['form']=form
    return render(request,"roomservice/add.html",context)

def updateroomservice(request,id):
    context={}
    obj=get_object_or_404(roomserviceModel,id=id)
    form=roomserviceForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewroomservice")
    context["form"]=form
    return render(request,"roomservice/edit.html",context)

def deleteroomservice(request,id):
    context={}
    obj=get_object_or_404(roomserviceModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewroomservice")
    return render(request,"roomservice/view.html",context)