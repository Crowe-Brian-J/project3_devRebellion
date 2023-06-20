from django.db import models
from django.urls import reverse
from django.views.generic.edit import CreateView

from django.contrib.auth.models import User
from django.db.models.signals import post_save

#inspired from codemy.com for user, and profiles
class Developer(models.Model):    #also shown as profiles. One user to one profile 
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    print(user)
    
    def __str__(self):
        return f'{self.user.username} ({self.user.id})'

    def get_absolute_url(self):
        return reverse('index', kwargs={'developer_id': self.id})


class Project(models.Model):
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.id})"

    def get_absolute_url(self):
        return reverse("projects_detail", kwargs={"project_id": self.id})

class Comment(models.Model):
    content = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment {self.id} on Project {self.project_id}"

class Feed(models.Model):
    text = models.TextField()
    developer = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.text} ({self.id})"

    def get_absolute_url(self):
        return reverse("detail", kwargs={"feed_id": self.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"Photo for project_id: {self.project_id} @{self.url}."
