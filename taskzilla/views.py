from django.shortcuts import render

from .models import Task

def index(request):
	tasks_list = Task.objects.all()
	context = {'tasks_list' : tasks_list,}	
	return render(request, 'taskzilla/index.html', context)

def task_page(request, task_id):
	task = Task.objects.get(pk=task_id)
	context = {'task' : task}
	return render(request, 'taskzilla/task_page.html', context)
