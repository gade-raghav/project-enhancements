from django.urls import path
from . import views

urlpatterns = [
    #--DEMO url
    path('', views.home, name="home"),

    #--Project based urls
    path('newproject', views.newproject, name="newproject"),
    path('welcome', views.welcome, name="welcome"),
    path('feedback', views.feedback, name="feedback"),

]