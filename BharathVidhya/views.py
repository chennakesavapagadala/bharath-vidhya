from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
import random
from django.http import HttpResponse
from django.http import JsonResponse

from .scrape import *
from .csvdata import *
import pandas as pd
import csv
# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['uname']
        email = request.POST['email']
        password1 = request.POST['pwd1']
        password2 = request.POST['pwd2']
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            messages.success(request, f"Hello, {username} Successfully Created Your Account")
            return redirect('signin')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'UserName is Already Exist..')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email Id is Already Exist..')
        else:
            messages.info(request, 'Passwords Did Not Match')
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pwd']
        username = User.objects.get(email=email).username
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Password Or UserName')
    return render(request, 'signin.html')

@never_cache
@login_required(login_url='signin')
def signout(request):
    auth.logout(request)
    return redirect('home')

@never_cache
@login_required(login_url='signin')
def newuser(request):
    auth.logout(request)
    return redirect('signup')

def home(request):

    context = {
        'top_colleges':top_colleges,
        'all_colleges':all_colleges,
        'private_colleges':private_colleges,
        'government_colleges':government_colleges,
    }
    return render(request, 'home.html',context)

@never_cache
@login_required(login_url='signin')
def colleges(request):

    context = {
        'top_colleges':top_colleges,
        'all_colleges':all_colleges,
        'private_colleges':private_colleges,
        'government_colleges':government_colleges,
    }
    return render(request, 'colleges.html',context)

@never_cache
@login_required(login_url='signin')
def private(request):
    context = {
        'top_colleges':top_colleges,
        'all_colleges':all_colleges,
        'private_colleges':private_colleges,
        'government_colleges':government_colleges,
    }
    return render(request, 'private.html',context)

@never_cache
@login_required(login_url='signin')
def govt(request):
    context = {
        'top_colleges':top_colleges,
        'all_colleges':all_colleges,
        'private_colleges':private_colleges,
        'government_colleges':government_colleges,
    }
    return render(request, 'govt.html',context)

@never_cache
@login_required(login_url='signin')
def top_clgs(request):
    context = {
        'top_colleges':top_colleges,
        'all_colleges':all_colleges,
        'private_colleges':private_colleges,
        'government_colleges':government_colleges,
    }
    return render(request, 'top-clgs.html',context)
