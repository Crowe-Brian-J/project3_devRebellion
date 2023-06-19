from django.shortcuts import render
from .models import Project, Feed
from django.views.generic.edit import CreateView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


class ProjectCreate(CreateView):
  model = Project
  fields = '__all__'
  