from django.db import models

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