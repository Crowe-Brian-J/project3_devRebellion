from django.forms import ModelForm
from .models import Comment, User, Developer
from django import forms 


class CommentForm(ModelForm):
    class Meta:
        model=Comment 
        fields=['text']

class UserForm(forms.ModelForm):
    class Meta: 
        model = User
        fields =('first_name', 'last_name', 'email')

class DeveloperForm(forms.ModelForm):
    class Meta: 
        model = Developer
        fields = ('link',)
