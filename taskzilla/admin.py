from django.contrib import admin

# Register your models here.

# from django.contrib.auth.models import User
from .models import Task, UserProfile

# admin.site.register(User)
admin.site.register(Task)
admin.site.register(UserProfile)