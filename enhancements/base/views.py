from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *   
from .forms import *
from .decorators import *

#---Home
@login_required(login_url='signin')
def home(request):
    projects = Project.objects.all()
    progress = Progress.objects.all()
    context = {
        'projects' : projects,
        'progress' : progress
    }
    return render(request,'base/projects.html',context)

#--Signin/Signout
@unauthenticated_user
def signin(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
            
        if user is not None:
            login(request,user)
            messages.info(request, 'Logged in successfully!')
            return redirect('welcome')
        else:
            messages.error(request,'username or password not correct')
            return redirect('signin')
    
    context = {
            'form': form
    }

    return render(request,'base/signin.html',context)

def signout(request):
    logout(request)
    messages.info(request, 'Logged out.')
    return redirect('signin')

#--PROJECT--#
#--new project form 
@login_required(login_url='signin')
def newproject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        

    context = {
        'form':form
    }

    return render(request,'base/newproject.html', context) 

def welcome(request):
    return render(request,'base/welcome.html')

def feedback(request):
    form = FeedbackForm
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {
        'form':form
    }
    return render(request, 'base/feedback.html', context)
