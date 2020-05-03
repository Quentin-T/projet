from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Project, Task, Status, Journal
from .forms import JournalForm, TaskForm


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

def newComment(request, id):
    form = JournalForm(request.POST or None)

    if form.is_valid():
        journal = Journal()
        journal.author = request.user
        journal.entry = form.cleaned_data["entry"]
        journal.task = Task.objects.get(id=id)
        journal.save()
        return redirect("task",id)
    return render(request, "newComment.html", locals())


def newtask(request, id):
    form = TaskForm(request.POST or None)

    if form.is_valid():
        task = Task(projet=Project.objects.get(id=id))
        task.name = form.cleaned_data['name']
        task.assignee = form.cleaned_data['assignee']
        task.description = form.cleaned_data['description']
        task.start_date = form.cleaned_data['start_date']
        task.due_date = form.cleaned_data['due_date']
        task.priority = form.cleaned_data['priority']
        task.status = form.cleaned_data['status']
        task.save()
        return redirect("task", task.id)
    return render(request, "newtask.html", locals())