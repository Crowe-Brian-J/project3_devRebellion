from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path(
        "developers/", views.developers_index, name="index"
    ),  # need to change to developers detail
    path("feeds/", views.feeds_index, name="feeds_index"),
    path("feeds/<int:feed_id>/", views.feeds_detail, name="feeds_detail"),
    path("projects/", views.projects_index, name="projects_index"),
    path(
        "projects/<int:project_id>/", views.projects_detail, name="detail"
    ),  # need to change to projects detail
    path('accounts/signup/', views.signup, name='signup'),
    path('projects/create/', views.ProjectCreate.as_view(), name='projects_create'),
]
