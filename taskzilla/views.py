from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Task

def index(request):
	tasks_list = Task.objects.filter(closed=False)
	context = {'tasks_list' : tasks_list,}	
	return render(request, 'taskzilla/index.html', context)

def task_page(request, task_id):
	task = Task.objects.get(pk=task_id)
	context = {'task' : task, 'comments': task.comment_set.all()}
	return render(request, 'taskzilla/task_page.html', context)

def login_page(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		print(user, username, password)
		if user is not None:
			login(request, user)
			return render(request, 'taskzilla/login.html', {'loggedin' : True})
	return render(request, 'taskzilla/login.html', {'loggedin': False})
