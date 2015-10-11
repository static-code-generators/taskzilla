from django.db import models
# import django.contrib.auth.models as auth
from django.contrib.auth.models import User
# from django.conf import settings

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)

	def __str__(self):
		return self.user.get_username()
	# tasks = models.ManyToManyField ('Task', related_name='subscribers')

class Task(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length = 100)
	description = models.TextField(default = '')
	pub_date = models.DateTimeField('date published')
	subscribers = models.ManyToManyField(UserProfile, related_name='tasks')
	closed = models.BooleanField(default=False)

	def __str__(self):
		return self.title

class Comment(models.Model):
	id = models.AutoField(primary_key=True)
	text = models.TextField(default = '')
	task = models.ForeignKey(Task)
	user = models.ForeignKey(UserProfile, default = '')


# class UserTask(models.Model):
#	task = models.ForeignKey(Task)
#	# user = models.ForeignKey(settings.AUTH_USER_MODEL)
#	user = models.ForeignKey(UserProfile)
