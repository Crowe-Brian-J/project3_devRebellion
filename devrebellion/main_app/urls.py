from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("developers/", views.developers_index, name="index"),
    path("feeds/", views.feeds_index, name="feeds_index"),
]
