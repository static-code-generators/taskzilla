from django.contrib import admin

# Register your models here.

# from django.contrib.auth.models import User
from .models import Task, UserProfile, Comment

class CommentInline(admin.StackedInline):
	model = Comment
	extra = 0

class TaskAdmin(admin.ModelAdmin):
	inlines = [CommentInline]

# admin.site.register(User)
admin.site.register(Task, TaskAdmin)
admin.site.register(UserProfile)
#admin.site.register(Comment)

