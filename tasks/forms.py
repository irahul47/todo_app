from django import forms
from django.forms import ModelForm

from .models import *

# Form Representation of Model

# When we specify which model we're gonna replicate, it's gonna create all the form fields for us.

class TaskForm(forms.ModelForm):

    title = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Add new task...'}))

    class Meta:
        model = Task 
        fields = '__all__' 
