from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from django.utils import timezone


def index(request):
    tasks = Todo.objects.all().order_by("is_complete", "-priority", "-date")
    return render(request, 'index.html', {'tasks': tasks})


@csrf_exempt
def add_todo(request):
    task_name = request.POST["task_name"]
    task_priority = request.POST["task_priority"]
    Todo.objects.create(text=task_name, date=timezone.now(),
                        priority=task_priority)
    return HttpResponseRedirect("/")


@csrf_exempt
def delete_todo(request, task_id):
    Todo.objects.get(id=task_id).delete()
    return HttpResponseRedirect("/")


@csrf_exempt
def complete_todo(request, task_id):
    task = Todo.objects.get(id=task_id)
    task.is_complete = True
    task.save()
    return HttpResponseRedirect("/")


@csrf_exempt
def edit_todo(request, task_id):
    task = Todo.objects.get(id=task_id)
    task.text = request.POST["view_task_name"]
    task.priority = request.POST["view_task_priority"]
    task.save()
    return HttpResponseRedirect("/")
