from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Project(models.Model):
    # le nom du projet
    name = models.CharField(max_length=200)
    # les utilisateurs qui participent au projet
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Status(models.Model):
    # le nom du statut
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Task(models.Model):
    # le projet auquel la tache est rattachée
    projet = models.ForeignKey(Project, on_delete=models.CASCADE)
    # le nom de la tache
    name = models.CharField(max_length=200)
    # une description de la tache
    description = models.CharField(max_length = 2000)
    # l'utilisateur assigne à la tache
    assignee = models.ForeignKey(User, on_delete=models.CASCADE)
    # date de début de la tache
    start_date = models.DateTimeField()
    # date de fin de la tache
    due_date = models.DateTimeField()
    # priorité de la tache
    priority = models.IntegerField()
    # statut de la tache
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class Journal(models.Model):
    # la date du commentaire
    date = models.DateTimeField()
    # le commentaire
    entry = models.CharField(max_length=300)
    # l'auteur du commentaire
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # la tahce concernée
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
