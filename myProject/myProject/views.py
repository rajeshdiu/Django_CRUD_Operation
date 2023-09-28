from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from myApp.models import Employees

def homePage(request):
    
    emp=Employees.objects.all()
    context={
         'emp':emp   
    }
    
    return render(request,"home.html",context)


def loginPage(request):
    
     if request.method=="POST":
        username=request.POST.get("username")
        pass1=request.POST.get("pass")
        user=authenticate(request,username=username,password=pass1)
        
        if user is not None:
            login(request,user)
            return redirect("homePage")
        else:
            return HttpResponse("username not found")
    
     return render(request,"login.html")


def SignupPage(request):

    if request.method=="POST":
        uname=request.POST.get("username")
        email=request.POST.get("email")
        pass1=request.POST.get("password1")
        pass2=request.POST.get("password2")
        
        if pass1!=pass2:
            return HttpResponse("Not Match")
        else:
            myuser=User.objects.create_user(uname,email,pass1)
            myuser.save()
            return redirect("loginPage")
        
        
    messages.success(request, 'Signup successful.')
    return render(request,"signup.html")


def addPage(request):

    if request.method=="POST":
        myName=request.POST.get("name")
        myEmail=request.POST.get("email")
        myAddress=request.POST.get("address")
        myPhone=request.POST.get("phone")
        
        emp=Employees(
            name=myName,
            email=myEmail,
            address=myAddress,
            mobile=myPhone
            
        )
        
        emp.save()
        return redirect("homePage")
        
        
    return render(request,"home.html")


def editPage(request):
    
    emp=Employees.objects.all()
    
    content={
        "emp":emp
    }
    
    return render(request,"home.html",content)



def updatePage(request,id):

    if request.method=="POST":
        myName=request.POST.get("name")
        myEmail=request.POST.get("email")
        myAddress=request.POST.get("address")
        myPhone=request.POST.get("phone")
        
        emp=Employees(
            id=id,
            name=myName,
            email=myEmail,
            address=myAddress,
            mobile=myPhone
            
        )
        
        emp.save()
        return redirect("homePage")
        
        
    return render(request,"home.html")


def deletePage(request,id):
    
    emp=Employees.objects.filter(id=id)
    emp.delete()
    
    
    content={
        "emp":emp
    }
    
    return redirect("homePage")
    