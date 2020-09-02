from django.contrib.auth.models import User
from django.db import models
from hashid_field import HashidAutoField

# Create your models here.

class Project(models.Model):
    STATUS = (
        ('Queued','Queued'),
        ('Working','Working'),
        ('Completed','Completed'),
    )

    project_id = HashidAutoField(min_length=8,primary_key=True,alphabet="0123456789abcdefghijklmnopqrstuvwxyz",salt="drop the gun and go to steam bathc")
    project_title = models.CharField(max_length=200,default='New Project')
    project_description = models.TextField(max_length=2000,default='Project Description')
    github_link = models.CharField(max_length=200, default='',blank=True,null=True)
    status = models.CharField(max_length=20,null=False,choices=STATUS,default="Working") 
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.project_id)

class Feature(models.Model):
    STATUS = (
        ('Queued','Queued'),
        ('Working','Working'),
        ('Discarded','Discarded'),
        ('Completed','Completed'),
    )
    feature_id = models.ForeignKey(Project,null=True,on_delete=models.CASCADE)
    tracking_id = HashidAutoField(min_length=8,primary_key=True,alphabet="0123456789abcdefghijklmnopqrstuvwxyz",salt="Sakura says but she doesn't mean it bolte") 
    feature_name = models.CharField(max_length=50,null=False,default='New Feature')
    feature_description = models.TextField(max_length=500,null=False,default='Feature Description')
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,null=False,choices=STATUS,default="Queued")

    def __str__(self):
        return '%s-->' '%s' % (str(self.feature_id),str(self.tracking_id))

class Progress(models.Model):
    tracking = models.ForeignKey(Feature,null=True,on_delete=models.CASCADE)
    trackerid = HashidAutoField(min_length=8,primary_key=True,alphabet="0123456789abcdefghijklmnopqrstuvwxyz",salt="Gamatatsu Niichan are Naruto summons")  
    date_created = models.DateTimeField(auto_now_add=True)
    tracker_title = models.CharField(max_length=50,null=False,default='Progress')
    tracker_description = models.TextField(max_length=200,null=False,default='Description')

    def __str__(self):
        return str(self.tracking)
    
    