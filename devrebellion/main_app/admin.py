from django.contrib import admin

from .models import Project, Feed, Photo

admin.site.register(Project)
# Register your models here.
admin.site.register(Feed)
admin.site.register(Photo)
