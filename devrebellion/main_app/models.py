from django.db import models
from django.urls import reverse
from django.views.generic.edit import CreateView

from django.contrib.auth.models import User
from django.db.models.signals import post_save

#inspired from codemy.com for user, and profiles

class Developer(models.Model):    #also shown as profiles. One user to one profile 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # follows= models.ManyToManyField("self",       #developers can follow several profiles
        # related_name="followed_by",
        # symmetrical=False,
        # blank=True)     #do not  have to have followers

    def __str__(self):
        return f'{self.name} ({self.id})'
#create profile(developer) when new user signs up

    # def create_developer(sender, instance, created, **kwargs):
    #     if created:
    #         user_developer = Developer(user=instance) #new user created
    #         user_developer.save()
    #     #Have the user follow themselves
    #     # user_developer.follows.set([instance.developer.id])
    #         user_profile.save()

    #     post_save.connect(create_developer, sender=User)
    

class Project(models.Model):
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.id})"

    def get_absolute_url(self):
        return reverse("projects_detail", kwargs={"project_id": self.id})


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
