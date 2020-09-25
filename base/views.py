from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import DeleteView
from .models import *   
from .forms import *
from .decorators import *



#--Error Pages
def error_500_view(request):
    return render(request,'500.html')

def error_404_view(request,exception):
    return render(request,'404.html')

#--Welcome Page
def welcome(request):
    return render(request,'base/welcome.html')


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
            return redirect('home')
        

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


#--Edit Project
@login_required(login_url='signin')
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

#--About Feature
def aboutfeature(request,tracking_id):
    feature = Feature.objects.get(tracking_id=tracking_id)
    #--Adding new progress form--
    progress = Progress.objects.all()
    form = ProgressForm()
    if request.method == 'POST':
        form= ProgressForm(request.POST)
        if form.is_valid():
            user = request.user
            prog = form.save(commit=False)
            prog.user = User.objects.get(username=user)
            prog.tracking = Feature.objects.get(tracking_id=tracking_id)
            prog.save()
            return HttpResponseRedirect(request.path_info)

    count=0
    counter=0
    for a in progress:
        if a.tracking.tracking_id == tracking_id:
            if a.comment_type == "Task":
                count=count+1
                if a.task_completed:
                    counter = counter+1
    if count != 0:
        percent = (counter/count)*100
    else: percent = 0
    context = {
        'feature' : feature,
        'form': form,
        'progress' : progress,
        'percent' : percent,
        'counter' : counter,
        'count' : count,

    }
    return render(request,'base/specificfeature.html',context)

#--Progress comments edit
def editprogress(request,trackerid):
    progress = Progress.objects.get(trackerid=trackerid)
    form = ProgressForm(instance=progress)

    if request.method == 'POST':
        form = ProgressForm(request.POST, request.FILES, instance=progress)
        if form.is_valid():
            form.save()
            messages.info(request, 'Updated.')
            return redirect('features')

    context ={
        'form' : form
    }

    return render(request,'base/editprogress.html',context)

#--New feature form
@login_required(login_url='signin')
def newfeature(request):
    form = FeatureForm()
    if request.method == 'POST':
        form = FeatureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('features')
        

    context = {
        'form':form
    }

    return render(request,'base/newfeature.html', context) 

#--Edit Feature
@login_required(login_url='signin')
def featureedit(request,tracking_id):
    feature = Feature.objects.get(tracking_id=tracking_id)
    form = FeatureForm(instance=feature)

    if request.method == 'POST':
        form = FeatureForm(request.POST, request.FILES, instance=feature)
        if form.is_valid():
            form.save()
            messages.info(request, 'Updated.')
            return redirect('features')

    context = { 

        'form' : form,
        'feature': feature

        }


    return render(request,'base/featureedit.html', context)

def aboutme(request):

    profile = Aboutme.objects.get(id=3)

    context = {
        'profile' : profile
    }

    return render(request,'base/profile.html', context)

def aboutmeedit(request,):
    profile = Aboutme.objects.get(name="Raghav Gade")
    form = AboutmeForm(instance=profile)

    if request.method == 'POST':
        form = AboutmeForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.info(request, 'Updated.')
            return redirect('aboutme')

    context = { 

        'form' : form,

        }


    return render(request,'base/profileedit.html', context)


#--BLOG --#

def blog(request):
    blogs = Blog.objects.all()
    comments = BlogComments.objects.all()

    context = {
        'blogs' : blogs,
        'comments' : comments
    }

    return render(request,'base/blog.html', context)

def specificblog(request,id):

    blog = Blog.objects.get(id=id)

    context = {
        'blog' : blog
    }

    return render(request,'base/specificblog.html', context)

def newblog(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
        

    context = {
        'form':form
    }

    return render(request,'base/newblog.html', context) 

def blogedit(request,id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(instance=blog)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.info(request, 'Updated.')
            return redirect('blog')

    context = { 

        'form' : form,
        'blog' : blog,

    }

    return render(request,'base/blogedit.html', context)

def deleteblog(request,id):
    blog = Blog.objects.get(id=id)

    if request.method=="POST":
        blog.delete()
        messages.success(request, 'Blog successfully deleted')
        return redirect('blog')

    return render(request, 'base/deleteblog.html')