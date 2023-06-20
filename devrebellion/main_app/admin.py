from django.contrib import admin
from django.contrib.auth.models import User 
from .models import Project, Feed, Photo, Developer 

admin.site.register(Project)
# Register your models here.
admin.site.register(Feed)
admin.site.register(Photo)
# admin.site.unregister(User) #unregister initial user
# admin.site.register(User)
admin.site.register(Developer)

#mix profile info into User info
# class DeveloperInline(admin.StackedInLine):
    # model = Developer

#extends User Model    
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"] #to display the usernames on the fields page
    # inlines = [DeveloperInLine]