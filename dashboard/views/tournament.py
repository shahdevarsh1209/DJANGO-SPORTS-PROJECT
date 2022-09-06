from django.shortcuts import get_object_or_404,render,redirect
from ..models import tournamentModel
from django.shortcuts import render

from ..forms.tournament_form import tournamentForm


def viewtournament(request):
    context={}
    context["tournaments"]=tournamentModel.objects.all()
    return render(request, "tournament/view.html",context)

def addtournament(request):
    context={}
    form=tournamentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewtournament")
    context['form']=form
    return render(request,"tournament/add.html",context)

def updatetournament(request,id):
    context={}
    obj=get_object_or_404(tournamentModel,id=id)
    form=tournamentForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewtournament")
    context["form"]=form
    return render(request,"tournament/edit.html",context)

def deletetournament(request,id):
    context={}
    obj=get_object_or_404(tournamentModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewtournament")
    return render(request,"tournament/view.html",context)