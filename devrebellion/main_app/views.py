import uuid
import boto3
from django.shortcuts import render, redirect
from .models import Project, Feed, Photo, Developer, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

import os

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
    },
]


# Define the home view
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def developers_index(request):
    # might have to drop the filter because we want to see all developers
    # developers = Developer.objects.all()
    developers = User.objects.order_by('id')
    return render(request, 'developers/index.html',            
        {'developers': developers})

def developers_detail(request,developer_id):
    developers = Developer.objects.get(id=developer_id)
    return render(request,'developers/detail.html', {
        'developer': developer})


def projects_index(request):
    projects = Project.objects.all()
    print(projects)
    return render(request, "projects/index.html", {"projects": projects})


def projects_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == "POST":
        text = request.POST.get("comment_text")
        comment = Comment(project=project, text=text)
        comment.save()
        return redirect("projects_detail", project_id=project_id)

    comments = Comment.objects.filter(project=project).order_by("-timestamp")
    return render(request, "projects/detail.html", {"project": project, "comments": comments})


def add_projects_photo(request, project_id):
    photo_file = request.FILES.get("photo-file", None)
    if photo_file:
        s3 = boto3.client("s3")
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind(".") :]
        try:
            bucket = os.environ["S3_BUCKET"]
            print(bucket)
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to project_id or project (if you have a project object)
            Photo.objects.create(url=url, project_id=project_id)
        except Exception as err:
            print("An error occurred uploading file to S3")
            print(err)
            # 'S3_BUCKET'
    return redirect("projects_detail", project_id=project_id)


def add_comment(request, project_id):
    project = Project.objects.get(id=project_id)

def feeds_index(request):
    feeds = Feed.objects.all()
    return render(request, "feeds/index.html", {"feeds": feeds})


def feeds_detail(request, feed_id):
    feed = Feed.objects.get(id=feed_id)
    return render(request, "feeds/detail.html", {"feed": feed})


def signup(request):
    error_message = ""
    if request.method == "POST":
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            #add new registration page for developer, user sent to after they sign up, create a developer
            return redirect("developers_index")
        else:
            error_message = "Invalid sign up - try again"
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)


class ProjectCreate(CreateView):
    model = Project
    fields = "__all__"
    # success_url = "/projects/{project_id}"


class ProjectUpdate(UpdateView):
    model = Project
    fields = "__all__"


class ProjectDelete(DeleteView):
    model = Project
    success_url = "/projects"
