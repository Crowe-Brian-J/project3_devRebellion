import uuid
import boto3
from django.shortcuts import render, redirect
from .models import Project, Feed, Photo, Developer, Comment, FeedComment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .forms import CommentForm, UserForm, DeveloperForm, FeedCommentForm
from django.db import transaction
from django.contrib import messages
from django.utils.translation import gettext as _
from django.core.mail import send_mail


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


# @login_required
def developers_index(request):
    # might have to drop the filter because we want to see all developers
    # developers = Developer.objects.all()
    developers = Developer.objects.order_by("id")
    return render(request, "developers/index.html", {"developers": developers})


# @login_required
@transaction.atomic
def update_developer(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        developer_form = DeveloperForm(request.POST, instance=request.user)
        print(user_form)
        if user_form.is_valid() and developer_form.is_valid():
            user_form.save()
            developer_form.save()
            messages.success(request, _("Your profile was successfully updated!"))
            return redirect("developers_index")  # possible change to developer detail
        else:
            messages.error(request, _("Please correct the error below."))
    else:
        user_form = UserForm(instance=request.user)
        developer_form = DeveloperForm(instance=request.user.developer)
    return render(
        request,
        "registration/profile.html",
        {  # comeback to this line
            "user_form": user_form,
            "developer_form": developer_form,
        },
    )


# @login_required
def developers_detail(request, developer_user_id):
    developer = User.objects.get(id=developer_user_id)
    projects = Project.objects.filter(user=developer_user_id)
    feeds = Feed.objects.filter(user=developer_user_id)
    print(developer)
    return render(request, "developers/detail.html", {"developer": developer,
    "projects": projects, "feeds": feeds, "surfing_user": request.user.id
    })

# @login_required
def delete_developer(request, developer_user_id):
  if request.user.id == developer_user_id:
       developer = User.objects.get(id=developer_user_id)
       developer.delete()
       return redirect("about")
  else: 
        return redirect("developers_index")

# ----new edit ---
def edit_developer(request, developer_user_id):
    # developer = request.user.developer
    if request.method == 'POST':
        # d = User.objects.get(id=developer_user_id)
        user_form = UserForm(request.POST, instance=request.user)
        developer_form = DeveloperForm(request.POST, instance=request.user)
        print(developer_form, "this is a developer form")
        if user_form.is_valid() and developer_form.is_valid():
            print('user')
            user_form.save()
            developer_form.save()
            return redirect('developers_detail', developer_user_id)
    else: 
        d = User.objects.get(id=developer_user_id)
        user_form = UserForm(request.POST, instance=request.user)
        developer_form = DeveloperForm(request.POST, instance=request.user)
    return render(
        request,
        "registration/profile.html",
        {  # comeback to this line
            "user_form": user_form,
            "developer_form": developer_form,
            
        },
    )
def projects_index(request):
    projects = Project.objects.all()
    print(projects)
    return render(request, "projects/index.html", {"projects": projects})


def projects_detail(request, project_id):
    project = Project.objects.get(id=project_id)

    # if request.method == "POST":
    #     text = request.POST.get("comment_text")
    #     comment = Comment(project=project, text=text)
    #     comment.save()
    #     return redirect("projects_detail", project_id=project_id)
    comment_form = CommentForm()

    comments = Comment.objects.filter(project=project).order_by("-timestamp")
    return render(
        request,
        "projects/detail.html",
        {"project": project, "comments": comments, "comment_form": comment_form},
    )


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
    form = CommentForm(request.POST)
    project = Project.objects.get(id=project_id)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.user = request.user
        new_comment.project = project
        new_comment.save()

    return redirect("projects_detail", project_id=project_id)


def feeds_index(request):
    feeds = Feed.objects.all()
    return render(request, "feeds/index.html", {"feeds": feeds})


def feeds_detail(request, feed_id):
    feed = Feed.objects.get(id=feed_id)

    feed_comment_form = FeedCommentForm()

    feed_comments = FeedComment.objects.filter(feed=feed).order_by("timestamp")

    return render(
        request,
        "feeds/detail.html",
        {
            "feed": feed,
            "feed_comment_form": feed_comment_form,
            "feed_comments": feed_comments,
        },
    )


def add_feed_comment(request, feed_id):
    form = FeedCommentForm(request.POST)
    feed = Feed.objects.get(id=feed_id)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.user = request.user
        new_comment.feed = feed
        new_comment.save()

    return redirect("feeds_detail", feed_id=feed_id)


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
            # add new registration page for developer, user sent to after they sign up, create a developer
            return redirect("update_developer")
        else:
            error_message = "Invalid sign up - try again"
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)


class ProjectCreate(CreateView):
    model = Project
    fields = "__all__"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # success_url = "/projects/{project_id}"


class ProjectUpdate(UpdateView):
    model = Project
    fields = "__all__"


class ProjectDelete(DeleteView):
    model = Project
    success_url = "/projects"


class FeedCreate(CreateView):
    model = Feed
    fields = ["name", "text"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FeedUpdate(UpdateView):
    model = Feed
    fields = "__all__"


class FeedDelete(DeleteView):
    model = Feed
    success_url = "/feeds"


def send_invite(request):
    if request.method == "POST":
        email = request.POST.get("email")  # Get the email entered by the user
        subject = "Join the Rebellion"
        message = """We are excited to invite you to join DevRebellion, a vibrant community of passionate developers like yourself. 
                     With DevRebellion, you can connect with like-minded individuals, participate in coding challenges, and unlock endless opportunities to enhance your skills and showcase your talent. 
                     Join us today and let's embark on an epic coding journey together!"""

        send_mail(
            subject, message, "devrebellion@outlook.com", [email], fail_silently=False
        )
        success_message = "Invitation sent successfully!"
        return render(
            request, "invite/invite.html", {"success_message": success_message}
        )
    else:
        return render(request, "invite/invite.html")
