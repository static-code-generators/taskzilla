from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Task, Comment, UserProfile

def index(request):
	tasks_list = Task.objects.filter(closed=False)
	context = {'tasks_list' : tasks_list, 'user' : request.user,}
	return render(request, 'taskzilla/index.html', context)

def task_page(request, task_id):
	try:
		task = Task.objects.get(pk=task_id)
	except ObjectDoesNotExist:
		return HttpResponseRedirect('/')
	subscribed = (request.user.is_authenticated() and task.subscribers.filter(user=request.user).count() > 0)
	context = {'task' : task, 'comments': task.comment_set.all(), 'user' : request.user, 'subscribed' : subscribed}

	if request.method == 'POST' and request.user.is_authenticated():
		user = UserProfile.objects.get(user=request.user)
		comment_text = request.POST['text']
		comment = Comment()
		comment.text = comment_text
		comment.task = task
		comment.user = user
		comment.save()
		return HttpResponseRedirect('/tasks/' + str(task_id))

	return render(request, 'taskzilla/task_page.html', context)

@login_required(login_url = '/login/')
def subscribe(request, task_id):
	try:
		user = UserProfile.objects.get(user=request.user)
		task = Task.objects.get(id=task_id)
	except ObjectDoesNotExist:
		return HttpResponseRedirect('/')

	task.subscribers.add(user)
	return HttpResponseRedirect('/tasks/' + str(task_id))

@login_required(login_url = '/login/')
def unsubscribe(request, task_id):
	try:
		user = UserProfile.objects.get(user=request.user)
		task = Task.objects.get(id=task_id)
	except ObjectDoesNotExist:
		return HttpResponseRedirect('/')

	if (task.subscribers.filter(user=request.user).count() > 0):
		task.subscribers.remove(user)
	return HttpResponseRedirect('/tasks/' + str(task_id))	

def login_page(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		print(user, username, password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/')
		else:
			return render(request, 'taskzilla/login.html')
	return render(request, 'taskzilla/login.html')

def profile_page(request, username):
	try:
		user = UserProfile.objects.get(user__username=username)
	except ObjectDoesNotExist:
		return HttpResponseRedirect('/')
	context = {'user' : request.user, 'user_view' : user, }
	return render(request, 'taskzilla/profile_page.html', context)

def signup_page(request):
	context = {'error_msg' : None, 'display' : None}

	if request.user.is_authenticated():
		return HttpResponseRedirect('/')

	if request.method == 'POST':
		username = request.POST['username']
		if UserProfile.objects.filter(user__username=username).exists():
			context['error_msg'] = 'Username already taken :/'
			return render(request, 'taskzilla/signup.html', context)
		password = request.POST['password']
		passwordRe = request.POST['passwordRe']
		if password != passwordRe:
			context['error_msg'] = 'Passwords do not match'
			return render(request, 'taskzilla/signup.html', context)
		# Username is free to be alotted, and the passwords match
		up = UserProfile()
		up.user = User.objects.create_user(username=username, password=password)
		up.user.save()
		up.save()
		context['display'] = 'Your registeration was successful. You can try logging in now.'
		return render(request, 'taskzilla/signup.html', context)

	return render(request, 'taskzilla/signup.html', context)

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')
