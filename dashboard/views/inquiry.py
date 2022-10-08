from django.shortcuts import get_object_or_404,render,redirect
from ..models import inquiryModel
from django.shortcuts import render
from django.contrib import messages



from ..forms.inquiry_form import inquiryForm


def viewinquiry(request):
    context={}
    context["inquirys"]=inquiryModel.objects.all()
    return render(request, "inquiry/view.html",context)

def addinquiry(request):
    context={}
    form=inquiryForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.INFO,'Successfully Created')
        return redirect( "viewinquiry")
    context['form']=form
    return render(request,"inquiry/add.html",context)

def updateinquiry(request,id):
    context={}
    obj=get_object_or_404(inquiryModel,id=id)
    form=inquiryForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewinquiry")
    context["form"]=form
    return render(request,"inquiry/edit.html",context)

def deleteinquiry(request,id):
    context={}
    obj=get_object_or_404(inquiryModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewinquiry")
    return render(request,"inquiry/view.html",context)