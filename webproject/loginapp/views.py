from django.shortcuts import render,redirect
from.models import *
from.forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django. contrib import messages



# Create your views here.

def index(request):
    return render(request,'index.html')

def Register(request):
    if request.method == 'POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        myuser=User.objects.create_user(username=username,email=email,password=password)
        myuser.is_staff=True
        myuser.first_name=name
        myuser.save()
        return redirect('Login')
    
    else:
        form=UserCreationForm()
        return render(request,'authentication/register.html',{})

def login_user(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        myuser=authenticate(request,username=username,password=password)
        if myuser is not None:
            login(request,myuser)
            return redirect('index')
        else:
            messages.error(request, "somthing erroe...!")
            return redirect('Login')
    else:    
        return render(request,'authentication/login.html',{})

    return redirect('home')
def logout_user(request):
     return redirect('register')
    
