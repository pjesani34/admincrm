from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    #check to see if logged in
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "You Have Been Logged In")
            return redirect('index')
        else:
            messages.success(request, "There was An Error Logging In, Please Try Again!!")
            return redirect('index')
    else:
        return render(request, 'index.html', {})

def logout_user(request):        
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('index')

def register_user(request):
    return render(request, 'register.html', {})