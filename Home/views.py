from django.shortcuts import render
from .models import *
# Create your views here.

def our_work(request):
    # get a collection of all, projects.
    projects = Project.objects.all()

    return render(request, "our_work.html", {'projects': projects})

def project_details(request, pk):
    # get the project, based off of the pk that we passed in.
    project = Project.objects.filter(pk=pk).get()

    # query all of the images belonging to this proejct.
    images = ProjectGallery.objects.filter(project_id=pk)
    return render(request, "project_details.html", {'project': project, 'images': images})

def home(request):
    return render(request, "index.html")
