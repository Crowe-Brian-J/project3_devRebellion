from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("developers/", views.developers_index, name="developers_index"),
    path("developers/<int:developer_id>/", views.developers_detail, name='detail'),
    path("feeds/", views.feeds_index, name="feeds_index"),
    path("feeds/<int:feed_id>/", views.feeds_detail, name="feeds_detail"),
    path("projects/create/", views.ProjectCreate.as_view(), name="projects_create"),
    path("projects/", views.projects_index, name="projects_index"),
    path("projects/<int:project_id>/", views.projects_detail, name="projects_detail"),
    path(
        "projects/<int:pk>/update/",
        views.ProjectUpdate.as_view(),
        name="projects_update",
    ),
    path(
        "projects/<int:pk>/delete/",
        views.ProjectDelete.as_view(),
        name="projects_delete",
    ),
    path(
        "projects/<int:project_id>/add_projects_photo/",
        views.add_projects_photo,
        name="add_projects_photo",
    ),
    path("accounts/signup/", views.signup, name="signup"),
    path('projects/<int:project_id>/add-comment/', views.add_comment, name='add_comment'),
]
