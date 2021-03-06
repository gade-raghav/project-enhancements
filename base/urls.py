from django.urls import path
from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    #--Signin/Signout url
    path('signin', views.signin,name="signin"),
    path('signout', views.signout,name="signout"),

    #--Project based urls
    path('projects', views.projects, name="home"),
    path('newproject', views.newproject, name="newproject"),
    path('project/<str:project_id>', views.aboutproject,name ='specificproject'),
    path('projectedit/<str:project_id>', views.projectedit, name="projectedit"),
    path('', views.welcome, name="welcome"),
    path('feedback', views.feedback, name="feedback"),
    url(r'mdeditor/', include('mdeditor.urls')),

    #--Features based urls
    path('features', views.features, name="features"),
    path('newfeature/<str:project_id>', views.newfeature, name="newfeature"),
    path('feature/<str:tracking_id>', views.aboutfeature,name='specificfeature'),
    path('featureedit/<str:tracking_id>', views.featureedit, name="featureedit"),

    #--Progress edit
    path('editprogress/<str:trackerid>',views.editprogress, name="editprogress"),

    #--Profile based url
    path('aboutme', views.aboutme,name="aboutme"),
    path('editaboutme', views.aboutmeedit, name="editaboutme"),

    #--Blog base url
    path('blogs', views.blog, name="blog"),
    path('newblog', views.newblog, name="newblog"),
    path('blog/<str:id>',views.specificblog, name="sblog"),
    path('blog/<str:id>/edit', views.blogedit, name="blogedit"),
    path('blog/<int:id>/delete',views.deleteblog, name="blogdelete"),

    #--Bugs url 
    path('tickets', views.tickets, name="tickets"),
    path('newticket', views.newticket, name="newticket"),
    path('ticket/<str:tracking_id>', views.specificticket, name="ticket"),
    path('ticket/<str:tracking_id>/edit', views.editticket, name="ticketedit"),

    #--Bugs admin url
    path('bugs/home',views.bughome,name="bughome"),



]

