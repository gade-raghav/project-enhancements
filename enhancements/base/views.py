from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import *   
from .forms import *

#---Home
def home(request):
    projects = Project.objects.all()
    progress = Progress.objects.all()
    context = {
        'projects' : projects,
        'progress' : progress
    }
    return render(request,'base/home.html',context)

#--PROJECT--#
#--new project form 
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
