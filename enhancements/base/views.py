from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *   
from .forms import *
from .decorators import *

#--Welcome Page
def welcome(request):
    return render(request,'base/welcome.html')





#--Signin/Signout--#
#--Signin
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
            return redirect('home')
        else:
            messages.error(request,'username or password not correct')
            return redirect('signin')
    
    context = {
            'form': form
    }

    return render(request,'base/signin.html',context)


#--Signout
def signout(request):
    logout(request)
    messages.info(request, 'Logged out.')
    return redirect('welcome')





#--PROJECT--#
#--Projects 
def projects(request):
    projects = Project.objects.all()
    progress = Progress.objects.all()
    context = {
        'projects' : projects,
        'progress' : progress
    }
    return render(request,'base/projects.html',context)


#--New project form
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


#--Particular project
def aboutproject(request,project_id):
    project = Project.objects.get(project_id=project_id)
    context = {
        'project' : project
    }

    return render(request,'base/specificproject.html',context)


#--Feedback form
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


#--Edit Project
def projectedit(request,project_id):
    project = Project.objects.get(project_id=project_id)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.info(request, 'Updated.')
            return redirect('home')

    context = { 'form' : form}

    return render(request,'base/projectedit.html', context)





#--FEATURES--#
#--Features
def features(request):
    projects = Project.objects.all()
    features = Feature.objects.all()
    
    context ={
        'projects' : projects,
        'features' : features,
    }

    return render(request,'base/features.html',context)