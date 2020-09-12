from django.contrib.auth.models import User
from django.forms import forms
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from hashid_field import HashidAutoField

from mdeditor.fields import MDTextField


# Create your models here.

class Framework(models.Model):
    framework_name = models.CharField(max_length=40,null=True)

    def __str__(self):
        return self.framework_name


class Language(models.Model):
    language_name = models.CharField(max_length=40,null=True)

    def __str__(self):
        return self.language_name


class Containerization(models.Model):
    container_name = models.CharField(max_length=40,null=True)

    def __str__(self):
        return self.container_name


class Database(models.Model):
    database_name = models.CharField(max_length=40,null=True)

    def __str__(self):
        return self.database_name


class Project(models.Model):
    STATUS = (
        ('Queued','Queued'),
        ('Working','Working'),
        ('Completed','Completed'),
    )

    project_id = HashidAutoField(min_length=8,primary_key=True,alphabet="0123456789abcdefghijklmnopqrstuvwxyz",salt="drop the gun and go to steam bathc")
    project_title = models.CharField(max_length=200,default='New Project')
    framework_used = models.ManyToManyField(Framework,blank=True)
    language_used = models.ManyToManyField(Language,blank=True)
    containerization_used = models.ManyToManyField(Containerization,blank=True)
    database_used = models.ManyToManyField(Database,blank=True)
    project_description = MDTextField()
    github_link = models.CharField(max_length=200, default='',blank=True,null=True)
    status = models.CharField(max_length=20,null=False,choices=STATUS,default="Working") 
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    features = models.BooleanField(default=False)

    def __str__(self):
        return str(self.project_title)

class Feature(models.Model):
    STATUS = (
        ('Working','Working'),
        ('Discarded','Discarded'),
        ('Completed','Completed'),
    )
    feature_id = models.ForeignKey(Project,null=False,on_delete=models.CASCADE)
    tracking_id = HashidAutoField(min_length=8,primary_key=True,alphabet="0123456789abcdefghijklmnopqrstuvwxyz",salt="Sakura says but she doesn't mean it bolte") 
    feature_name = models.CharField(max_length=50,null=False,default='New Feature')
    feature_description = MDTextField()
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,null=False,choices=STATUS,default="Queued")

    def __str__(self):
        return '%s-->' '%s' % (str(self.feature_id),str(self.feature_name))

class Progress(models.Model):
    tracking = models.ForeignKey(Feature,null=True,on_delete=models.CASCADE)
    trackerid = HashidAutoField(min_length=8,primary_key=True,alphabet="0123456789abcdefghijklmnopqrstuvwxyz",salt="Gamatatsu Niichan are Naruto summons")  
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tracker_description = models.TextField(max_length=200,null=False,default='Description')
    progress_percentage= models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])

    def __str__(self):
        return str(self.tracking)



class Feedback(models.Model):
    CHOICE1=(
        ('Extremely useful','Extremely useful'),
        ('Somewhat useful','Somewhat useful'),
        ('Not useful','Not useful'),

    )
    CHOICE2=(
        ('New feature suggestion','New feature suggestion'),
        ('General comments','General comments'),
        ('Bug / Something does not work as expected','Bug / Something does not work as expected'),
        ('Other (please specify)','Other (please specify)')
    )
    CHOICE3=(
        ('yes','yes'),
        ('no','no')
    )
    choice1 = models.CharField(max_length=100,null=False,choices=CHOICE1,default=None,blank=False)
    choice2 = models.CharField(max_length=100,null=False,choices=CHOICE2,default=None,blank=False)
    other = models.CharField(max_length=100,blank=True)
    feedback = models.TextField(max_length=5000,null=False)
    email = models.EmailField(max_length=50)
    choice3 = models.CharField(max_length=4,choices=CHOICE3,default=None,blank=False)
    date_created = models.DateTimeField(auto_now_add=True)


class Aboutme(models.Model):
    email = models.CharField(max_length=200,default='',editable="false")
    name = models.CharField(max_length=100,null=True)
    igname = models.CharField(max_length=100,null=True,blank=True)
    githubid = models.CharField(max_length=100,null=True,blank=True)
    aboutme = MDTextField(null=True) 

    def __str__(self):
        return self.email