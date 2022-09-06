from django.shortcuts import get_object_or_404,render,redirect
from ..models import CategoryModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.category_form import CategoryForm
#from ..models import Category

def viewCategory(request):
    context={}
    context["categories"]=CategoryModel.objects.all()
    return render(request, "category/view.html",context)

def addCategory(request):
    context={}
    form=CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewCategory")
    context['form']=form
    return render(request,"category/add.html",context)

def updateCategory(request,id):
    context={}
    obj=get_object_or_404(CategoryModel,id=id)
    form=CategoryForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewCategory")
    context["form"]=form
    return render(request,"category/edit.html",context)

def deleteCategory(request,id):
    context={}
    obj=get_object_or_404(CategoryModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewCategory")
    return render(request,"category/view.html",context)