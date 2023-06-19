from django.db import models
from django.urls import reverse
from django.views.generic.edit import CreateView

from django.contrib.auth.models import User

# Create your models here.
# class Developer(models.Model):
#   name = models.CharField(max_length=100)
#   username = models.Charfield(max_length=150)
#   email = models.TextField(max_length=200)
#   links = models.


class Project(models.Model):
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.id})"

    def get_absolute_url(self):
        return reverse("detail", kwargs={"project_id": self.id})


class Feed(models.Model):
    text = models.TextField()
    developer = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.text} ({self.id})"

    def get_absolute_url(self):
        return reverse("detail", kwargs={"feed_id": self.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)

    def __str__(self):
        return (
            f"Photo for image: {self.url}. Needs to return foreign key at some point."
        )
    

class ProjectCreate(CreateView):
  model = Project
  fields = '__all__'
  success_url = '/project/{project_id}'
