from django.shortcuts import render, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": projects,
    }
    return render(request, "projects/list.html", context)
