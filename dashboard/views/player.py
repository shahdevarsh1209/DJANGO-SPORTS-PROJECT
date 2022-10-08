from django.shortcuts import get_object_or_404,render,redirect,HttpResponse
from ..models import playerModel
from django.shortcuts import render
from django.contrib import messages

from ..forms.player_form import playerForm


def viewplayer(request):
    context={}
    context["players"]=playerModel.objects.all()
    return render(request, "player/view.html",context)

def addplayer(request):
    context={}
    form=playerForm(request.POST or None)
    if form.is_valid():
        if len(request.FILES) != 0:
            form.img2 = request.FILES['img2']
        form.save()
        messages.add_message(request,messages.INFO,'Successfully Created')
        return redirect( "viewplayer")
    context['form']=form
    return render(request,"player/add.html",context)

def updateplayer(request,id):
    context={}
    obj=get_object_or_404(playerModel,id=id)
    form=playerForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewplayer")
    context["form"]=form
    return render(request,"player/edit.html",context)

def deleteplayer(request,id):
    context={}
    obj=get_object_or_404(playerModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewplayer")
    return render(request,"player/view.html",context)