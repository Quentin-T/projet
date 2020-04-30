from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def projects(request):
    "affichage des projets de l'utilisateur"
    return render(request,"projects.html", {'projets':request.user.project_set.all()})

# def project(request):
#     "affichage des différentes taches d'un projet précis"




