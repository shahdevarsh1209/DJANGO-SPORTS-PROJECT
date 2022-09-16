from django.shortcuts import render,redirect
#from django.http import HttpResponce

def homepage(request):
    return render(request,'homepage.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def evaluation(request):
    return render(request,'evaluation.html')

def feedback(request):
    return render(request,'feedback.html')

def inquiry(request):
    return render(request,'inquiry.html')

def main(request):
    return render(request,'main.html')

def matches(request):
    return render(request,'matches.html')

def players(request):
    return render(request,'players.html')

def single(request):
    return render(request,'single.html')

def tournament(request):
    return render(request,'tournament.html')

