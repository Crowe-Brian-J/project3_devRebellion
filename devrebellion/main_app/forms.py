from django.forms import ModelForm
from .models import Comment, User, Developer, Feed, FeedComment
from django import forms
from django.db import models

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ['link']


class FeedForm(forms.ModelForm):  # May need to just be ModelForm
    class Meta:
        model = Feed
        fields = (
            "name",
            "text",
        )


class FeedCommentForm(ModelForm):
    class Meta:
        model = FeedComment
        fields = ["text"]
