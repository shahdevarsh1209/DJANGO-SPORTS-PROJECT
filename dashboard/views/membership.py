from django.shortcuts import get_object_or_404,render,redirect
from ..models import membershipModel
from django.shortcuts import render
from django.contrib import messages

from ..forms.membership_form import membershipForm


def viewmembership(request):
    context={}
    context["memberships"]=membershipModel.objects.all()
    return render(request, "membership/view.html",context)

def addmembership(request):
    context={}
    form=membershipForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.INFO,'Successfully Created')
        return redirect( "viewmembership")
    context['form']=form
    return render(request,"membership/add.html",context)

def updatemembership(request,id):
    context={}
    obj=get_object_or_404(membershipModel,id=id)
    form=membershipForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewmembership")
    context["form"]=form
    return render(request,"membership/edit.html",context)

def deletemembership(request,id):
    context={}
    obj=get_object_or_404(membershipModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewmembership")
    return render(request,"membership/view.html",context)