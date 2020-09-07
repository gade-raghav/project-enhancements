from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm,forms,TextInput,Textarea,RadioSelect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django import forms
from .models import *




#--New project form
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['project_title','project_description','status','github_link','features']
        widgets ={

            'project_title' : TextInput(
                attrs={'placeholder':'Project Title'}),

            'project_description' : Textarea(
                attrs={'placeholder': 'Add project description'}
            )
    
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



class mdeditorForm (ModelForm):

    class Meta:
        model = ExampleModel
        fields = '__all__'