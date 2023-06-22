from django.urls import path
from . import views




urlpatterns = [
    # home urls
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    # developers urls
    path("developers/", views.developers_index, name="developers_index"),
    path(
        "developers/<int:developer_id>/",
        views.developers_detail,
        name="developers_detail",
    ),
    # feeds urls
    path("feeds/", views.feeds_index, name="feeds_index"),
    path("feeds/<int:feed_id>/", views.feeds_detail, name="feeds_detail"),
    path("feeds/create/", views.FeedCreate.as_view(), name="feeds_create"),
    path("feeds/<int:pk>/update", views.FeedUpdate.as_view(), name="feeds_update"),
    path("feeds/<int:pk>/delete", views.FeedDelete.as_view(), name="feeds_delete"),
    path(
        "feeds/<int:feed_id>/add_feed_comment/",
        views.add_feed_comment,
        name="add_feed_comment",
    ),
    # projects urls
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
    # accounts urls
    path("accounts/signup/", views.signup, name="signup"),
    # move to projects urls
    path(
        "projects/<int:project_id>/add-comment/", views.add_comment, name="add_comment"
    ),
    path("accounts/profile", views.update_developer, name="update_developer"),
    path('invite/', views.send_invite, name='send_invite'),
    
]
