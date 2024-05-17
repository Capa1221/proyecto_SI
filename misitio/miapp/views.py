from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
def saludo (request) :
    return HttpResponse ('Hola Mundo')

def consulta(request):
    tareas = models.Task.objects.all()
    for i in tareas:
        print(f'titulo: {i.title} FK: {i.project.name}')
    return HttpResponse("consulta")

def hello (request, username):
    """print(username)
    return HttpResponse("<h1>Hola %s<h1>" % username)"""
    return render(request, 'index.html')
    
def projects (request):
    projects = list (models.Project.objects.values())
    return JsonResponse (projects, safe = False)

def tasks (request, id):
    # task = models.Task.onjects.get(id = id)
    task = get_object_or_404 (models.Task, id = id)
    return HttpResponse ('task: %s' % task.title)

def about(request):
    return render(request, 'about.html')
