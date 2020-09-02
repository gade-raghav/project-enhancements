from django.forms import ModelForm,forms
from django import forms
from .models import *




#--New project form
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['project_title','project_description','status','github_link']

        widgets ={

            'project_title' : forms.TextInput(
                attrs={'placeholder':'Project Title'}),

            'project_description' : forms.Textarea(
                attrs={'placeholder': 'Add project description'}
            )
    
            }

