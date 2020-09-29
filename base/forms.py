from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm,forms,TextInput,Textarea,RadioSelect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django import forms
from .models import *




#--Comment form
class CommentForm(ModelForm):
    class Meta:
        model = BlogComments
        fields = ['email','comment']
        labels = {
            'email': _('Email-ID'),

        }

        widgets ={

            'comment' : Textarea(
                attrs={'placeholder': 'Something on your mind?'}
            )
    
            }
        

#--Project form
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['project_title','hosted','language_used','framework_used','containerization_used','database_used','status','features','github_link','project_description']
        labels = {
            'features': _('Features (Enable this option to work with features.)'),
            'hosted': _('Hosted (Is this application hosted online?)')

        }
        widgets ={

            'project_title' : TextInput(
                attrs={'placeholder':'Project Title'}),

            'project_description' : Textarea(
                attrs={'placeholder': 'Add project description'}
            )
    
            }
        
#--Feature form
class FeatureForm(ModelForm):
    class Meta:
        model = Feature
        fields = ['feature_name','status', 'feature_description']

#        labels = {
#            'feature_id': _('Project'),

#        }
        widgets ={

            'feature_name' : TextInput(
                attrs={'placeholder':'Feature name'}),

            'project_description' : Textarea(
                attrs={'placeholder': 'Add feature description'}
            )
    
            }

#--PROGRESS--#
#--Progress form
class ProgressForm(ModelForm):
    class Meta:
        model = Progress
        fields = ['comment_type','task_completed','tracker_description']
        
        labels = {
            'tracker_description':_('Progress description'),
            'comment_type':_('Type'),
            'task_completed':_('Completed Task'),
        }

#--Feedback form
class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['choice1','choice2','other','feedback','choice3','email']
        
        labels = {
            'choice1': _('How useful do you find Enhancements?'),
            'choice2': _('This feed back is about:'),
            'choice3': _('Do you want us to respond to your survery?'),

        }
        widgets = {

            'other' : TextInput(
                attrs={'placeholder':'Specify other reason'}),
            
            'feedback' : Textarea(
                attrs={'placeholder':'Enter feedback here'}),

            'choice1': RadioSelect,
            'choice2': RadioSelect,
            'choice3': RadioSelect,
            
        }


        def __init__(self, *args, **kwargs):
            super(FeedbackForm, self).__init__(*args, **kwargs)
            self.fields['choice1'].empty_label = None

        def clean(self):
            email = self.cleaned_data.get('email')
            try:
                validate_email(email)
            except ValidationError as e:
                print(e)
            else:
                return self.cleaned_data

class AboutmeForm(ModelForm):
    class Meta:
        model = Aboutme 
        fields = '__all__'

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['blog_title','blog_description','blog']

###--Bug Tracker--###
class BugForm(ModelForm):
    class Meta:
        model = Bug
        fields = ['project','user_email','subject','bug_severity','bug_description','user_device_information']
        labels = {
            'user_email': _('Email'),
            'project': _('App'),

        }

        widgets ={

            'user_device_information' : Textarea(
                attrs={'placeholder':'In case it is a bug, please enter your device hardware/software information.\nThis should include:\nOS(OS version)\nSoftware requirements for this application with version'}),
    
            }


class BugcommentsForm(ModelForm):
    class Meta:
        model = BugComments
        fields = ['comment']
        labels = {
            'comment': _('')
        }
        widgets = {
            'comment' : Textarea(
                attrs={'placeholder': 'Add your comment here'}
            )
        }