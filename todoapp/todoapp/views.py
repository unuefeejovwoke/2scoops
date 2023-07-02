from django.shortcuts import redirect, render
from django.http import HttpResponse

from todoapp.models import Todo

# Create your views here.
def addtask(request):
    task = request.POST['task']
    Todo.objects.create(tasks=task)
    return redirect('home')