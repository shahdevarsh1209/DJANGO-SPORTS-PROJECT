'''from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages
import mysql.connector
from operator import itemgetter
# Create your views here.

def index(request):
    return render(request,'dashboard/index.html')

def welcome(req):
    return render(req,'welcome.html')

def login(req):
    con = mysql.connector.connect(host="localhost",user="root",password="",database="sports")
    cursor = con.cursor()
    con2 = mysql.connector.connect(host="localhost",user="root",password="",database="sports")
    cursor2 = con2.cursor()

    sqlcommand = "select email from dashboard_user"
    sqlcommand2 = "select password from dashboard_user"
    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)
    e=[]
    p=[]
    for i in cursor:
        e.append(i)
    for j in cursor2:
        p.append(j)
    res = list(map(itemgetter(0),e))
    res2 = list(map(itemgetter(0),p))
    print(res)
    if req.method=="POST":
        email = req.POST['email']
        password = req.POST['password']
        i=1
        k=len(res)
        while i < k:
            if res[i]==email and res2[i]==password:
                return render(req,'welcome.html',{'email':email})
                break
            i+=1
        else:
            messages.info(req,"Check email and password")
            return redirect('login')
    return render(req,'login.html')

def register(req):
    if req.method == "POST":
        user = User()

        user.fname = req.POST['fname']
        user.lname = req.POST['lname']
        user.email = req.POST['email']
        user.password = req.POST['password']
        user.repassword = req.POST['repassword']
        
        if user.password != user.repassword:
            return redirect('register')
        elif user.fname == "" or user.password == "":
            messages.info(req,'Some fields are empty')
            return redirect('register')
        else:
            user.save()
    return render(req,'register.html')'''