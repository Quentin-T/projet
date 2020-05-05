from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Project, Task, Status, Journal
from .forms import JournalForm, TaskForm


# Create your views here.
@login_required
def projects(request):
    "affichage des projets de l'utilisateur"
    return render(request, "projects.html", {'projets': request.user.project_set.all(), 'User': request.user})


@login_required
def project(request, proj_id):
    "affichage des différentes taches d'un projet précis"
    project = Project.objects.get(id=proj_id)
    return render(request, "project.html", {'project': project, 'tasks': project.task_set.all()})


@login_required
def task(request, task_id):
    "affichage des détails d'une tache"
    task = Task.objects.get(id=task_id)
    comments = task.journal_set.all()
    return render(request, "task.html", locals())


@login_required
def newjournal(request, task_id):
    "ajout d'une nouvelle entrée de journal"
    task = Task.objects.get(id=task_id)
    form = JournalForm(request.POST or None)

    if form.is_valid():
        "on attribue par défaut l'utilisateur qui ajoute le journal et la date de publication"
        journal = Journal()
        journal.author = request.user
        journal.entry = form.cleaned_data["entry"]
        journal.task = task
        journal.save()
        return redirect("task", task_id)
    return render(request, "newjournal.html", locals())


@login_required
def newtask(request, proj_id):
    form = TaskForm(request.POST or None)

    """on récupère le projet en cours"""
    project = Project.objects.get(id=proj_id)

    """on recupère les utilisateurs et status pour les sélectionner dans le formulaire"""
    status = Status.objects.all()
    users = User.objects.all()

    if form.is_valid():
        task = Task(projet=project)
        task.name = form.cleaned_data["name"]
        task.assignee = form.cleaned_data["assignee"]
        task.description = form.cleaned_data["description"]
        task.start_date = form.cleaned_data["start_date"]
        task.due_date = form.cleaned_data["due_date"]
        task.priority = form.cleaned_data["priority"]
        task.status = form.cleaned_data["status"]
        task.save()
        return redirect("task", task.id)
    return render(request, "newtask.html", locals())


@login_required
def edittask(request, task_id):
    task = Task.objects.get(id=task_id)
    """on initialise le formulaire avec le contenu de task"""
    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        task.name = form.cleaned_data['name']
        task.assignee = form.cleaned_data['assignee']
        task.description = form.cleaned_data['description']
        task.start_date = form.cleaned_data['start_date']
        task.due_date = form.cleaned_data['due_date']
        task.priority = form.cleaned_data['priority']
        task.status = form.cleaned_data['status']
        task.save()
        return redirect("task", task.id)
    return render(request, "edittask.html", locals())
