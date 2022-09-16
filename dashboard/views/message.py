from django.shortcuts import get_object_or_404,render,redirect
from ..models import messageModel
from django.shortcuts import render

from ..forms.message_form import messageForm


def viewmessage(request):
    context={}
    context["messages"]=messageModel.objects.all()
    return render(request, "message/view.html",context)

def addmessage(request):
    context={}
    form=messageForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewmessage")
    context['form']=form
    return render(request,"message/add.html",context)

def updatemessage(request,id):
    context={}
    obj=get_object_or_404(messageModel,id=id)
    form=messageForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewmessage")
    context["form"]=form
    return render(request,"message/edit.html",context)

def deletemessage(request,id):
    context={}
    obj=get_object_or_404(messageModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewmessage")
    return render(request,"message/view.html",context)