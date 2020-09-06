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
    path('md',views.mdeditor,name="md")

]
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)