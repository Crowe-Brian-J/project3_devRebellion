from django.shortcuts import render
from .models import Project

developers = [
    {
        "name": "Mayte Ozoria",
        "username": "Ozmayte",
        "email": "ozoria@gmail.com",
        "links": "insert Link",
    },
    {
        "name": "Ryan Crosby",
        "username": "RyanC",
        "email": "crosby@gmail.com",
        "links": "insert Link",
    }
]


posts = [
    {"user": "User 1", "text": "This is some text", "imagesource": ""},
    {
        "user": "User 2",
        "text": "This is some more text",
        "imagesource": "",
    },
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
    return render(request, 'projects/detail.html', { 'project': project })
 


def feeds_index(request):
    return render(request, "feeds/index.html", {"posts": posts})
