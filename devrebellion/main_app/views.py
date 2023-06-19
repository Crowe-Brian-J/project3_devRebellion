from django.shortcuts import render
from .models import Project, Feed

developers = [
    {
        "name": "Mayte Ozoria",
        "username": "Ozmayte",
        "email": "ozoria@gmail.com",
        "links": "insert Link",
    }
]


# Define the home view
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def developers_index(request):
    return render(request, "developers/index.html", {"developers": developers})


def projects_index(request):
    projects = Project.objects.all()
    return render(request, "projects/index.html", {"projects": projects})


def projects_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, "projects/detail.html", {"project": project})


def feeds_index(request):
    feeds = Feed.objects.all()
    return render(request, "feeds/index.html", {"feeds": feeds})


def feeds_detail(request, feed_id):
    feed = Feed.objects.get(id=feed_id)
    return render(request, "feeds/detail.html", {"feed": feed})
