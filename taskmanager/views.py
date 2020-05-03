from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Project, Task, Status

# Create your views here.
@login_required
def projects(request):
    "affichage des projets de l'utilisateur"
    return render(request,"projects.html", {'projets':request.user.project_set.all(), 'User':request.user})


def project(request, id):
    "affichage des différentes taches d'un projet précis"
    proj= Project.objects.get(id=id)
    return render(request,"project.html", {'project':proj,'tasks':proj.task_set.all()})

def task(request, id):
    "affichage des détails d'une tache"
    tk = Task.objects.get(id=id)
    comments = tk.journal_set.all()
    return render(request,"task.html", locals())



