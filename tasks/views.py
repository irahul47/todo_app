from django.shortcuts import render, redirect # Render function will render the template
from django.http import HttpResponse 

from .models import *
from .forms import *


# Create your views here.

# For setting up an URL Routing

# For Index / Home Page

def index(request):
    tasks = Task.objects.all() # Task = Model

    form = TaskForm()

    if request.method =='POST': 
        form = TaskForm(request.POST) 
        if form.is_valid(): 
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context) 


# For UpdateTask Page

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'tasks/update_task.html', context)

# For DeleteTask Page

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'tasks/delete.html', context)
    