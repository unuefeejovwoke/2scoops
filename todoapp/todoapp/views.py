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
    return redirect('home')

def edit_task(request, pk): 
    get_task = get_object_or_404(Todo, pk=pk)
    if request.method == "POST": 
        new_task = request.POST['tasks']
        get_task.tasks = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task,
        }
        return render(request, 'edit_task.html', context)
