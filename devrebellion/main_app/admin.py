from django.contrib import admin

from .models import Project, Feed

admin.site.register(Project)
# Register your models here.
admin.site.register(Feed)
