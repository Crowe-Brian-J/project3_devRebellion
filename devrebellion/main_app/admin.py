from django.contrib import admin
from django.contrib.auth.models import User 
from .models import Project, Feed, Photo, Developer 

admin.site.register(Developer)
admin.site.register(Project)
admin.site.register(Feed)
admin.site.register(Photo)


#extends User Model    
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"] #to display the usernames on the fields page
    # inlines = [DeveloperInLine]