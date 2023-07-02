from django.http import HttpResponse
from django.shortcuts import render

from todoapp.models import Todo

def home(request): 
    tasks = Todo.objects.filter(is_completed= False).order_by('-updated_at')
    completed_tasks = Todo.objects.filter(is_completed=True)
    context = {
        'tasks':tasks,
        'completed_tasks': completed_tasks,
    }
    return render(request, 'home.html', context)