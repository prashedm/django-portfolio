from django.shortcuts import render
from .models import Project, feed

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})
def home(request):
    feeds = feed.objects.all()
    return render(request, 'portfolio/home.html', {'feeds':feeds})
