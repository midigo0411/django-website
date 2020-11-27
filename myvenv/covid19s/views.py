from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Project
# Create your views here.


def index(request):
    covid19s = Project.objects
    return render(request, 'projects/index.html',{'covid19s':covid19s})


def detail(request,project_id):
    #print(project_id)
    project_detail = get_object_or_404(Project,pk=project_id)
    return render(request, 'projects/detail.html', {'Project':project_detail})


