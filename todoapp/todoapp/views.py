from django.shortcuts import get_object_or_404, redirect, render
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
    
def mark_as_done(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    task.is_completed = True
    task.save()
    return JsonResponse({'task':task.tasks})

def unmark(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    task.is_completed = False
    task.save()
    return render(request, 'home.html')
