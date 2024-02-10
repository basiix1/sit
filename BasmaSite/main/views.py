from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Comment, Rating
import sys
sys.path.append("..")
from service.models import Service
from django.http import HttpRequest, HttpResponse


def index(request):
    services = Service.objects.all()
    return render(request, 'main/index.html', {'services': services})

def home(request):
    services = Service.objects.all()
    return render(request, 'main/home.html', {'services': services})

def about(request):
    services = Service.objects.all()
    return render(request, 'main/about.html', {'services': services})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': projects})

from django.urls import reverse

def add_project(request):
    if request.method == 'POST':
        title = request.POST['title']
        image = request.FILES['image']
        content = request.POST['content']
        link = request.POST['link']
        project = Project.objects.create(title=title, image=image, content=content, link=link)
        return redirect(reverse('main:projects'))  
    return render(request, 'main/add_project.html')

def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        project.delete()
        return redirect(reverse('main:projects'))
    
    return render(request, 'main/delete_project.html', {'project': project})

def project_details(request, project_id):
    project = Project.objects.get(id=project_id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        content = request.POST.get('content')
        rating = request.POST.get('rating')
        
        if name and content and rating:
            comment = Comment.objects.create(project=project, name=name, content=content, rating=rating)
            comment.save()
            print(comment)
            return redirect('main:project_details', project_id=project.id)
    return render(request, 'main/project_details.html', {'project': project})


def delete_comment(request, project_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('main:project_details', project_id=project_id)

def anime_view(request: HttpRequest):

    return render(request, "main/anime.html")