from django.shortcuts import redirect, render
from django.http import HttpResponse

from todoapp.models import Todo
from django.http import JsonResponse

def addtask(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        Todo.objects.create(tasks=task)
        return JsonResponse({'task': task})
    else:
        return render(request, 'home.html')

