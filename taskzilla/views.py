from django.shortcuts import render

from .models import Task

def index(request):
	tasks_list = Task.objects.all()
	context = {'tasks_list' : tasks_list,}	
	return render(request, 'taskzilla/index.html', context)
