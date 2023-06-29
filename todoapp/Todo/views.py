from django.http import HttpResponse
from django.shortcuts import render

from todoapp.models import Todo

def home(request): 
    tasks = Todo.objects.filter(is_completed= False)
    context = {
        'tasks':tasks,
    }
    return render(request, 'home.html', context)