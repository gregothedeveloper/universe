from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .forms import taskCreateForm

from.models import Task  # Import the Task model from the app1 models.py file. This is done to access the data from the database.  # noqa: E501

# Create your views here.
def home (request):
    return HttpResponse('this is bretech solution website')

def index(request):
    context = {
        'name':'Bretech Solution Administrator'
    }
    return render(request, 'app1/index.html', context)

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'app1/tasks.html', {'tasks':tasks})

def task_detail(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'app1/detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = taskCreateForm(request.POST)
        if form.is_valid( ):
            form.save()
            return redirect('task')
    else:
        form = taskCreateForm()
    return render(request, 'app1/create.html', {'form': form})

def task_update(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        form = taskCreateForm(request.POST, instance=task)
        if form.is_valid( ):
            form.save()
            return redirect('task')
    else:
        form = taskCreateForm(instance=task)
    return render(request, 'app1/update.html', {'form': form})

def task_delete(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('task')
    return render(request, 'app1/delete.html', {'task': task})