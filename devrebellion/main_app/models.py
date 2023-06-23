from django.db import models
from django.urls import reverse
from django.views.generic.edit import CreateView
from datetime import datetime

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# inspired from codemy.com for user, and profiles
class Developer(models.Model):  # also shown as profiles. One user to one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=255, null=True, blank=True,)
   
 

    @receiver(post_save, sender=User)
    def create_developer(sender, instance, created, **kwargs):
        if created:
            Developer.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_developer(sender, instance,  **kwargs):
        instance.developer.save()
        

    def __str__(self):
        return f"{self.user} {self.link} ({self.user.id})"

    def get_absolute_url(self):
        return reverse("index", kwargs={"developer_id": self.id})

    # come back to this line
    def delete_developer(self, *args, **kwargs):
        super().delete(*args, **kwargs)


class Project(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.id})"

    def get_absolute_url(self):
        return reverse("projects_detail", kwargs={"project_id": self.id})


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(default=datetime.now, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment {self.id} on Project {self.project_id}"


class Feed(models.Model):
    name = models.CharField(max_length=100, default="No Title")
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return f"{self.text} ({self.id})"

    def get_absolute_url(self):
        return reverse("feeds_detail", kwargs={"feed_id": self.id})


class FeedComment(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return f"FeedComment {self.id} on Feed Post {self.feed_id}"


class Photo(models.Model):
    url = models.CharField(max_length=200)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"Photo for project_id: {self.project_id} @{self.url}."
