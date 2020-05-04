from django.urls import path
from . import views
urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<int:proj_id>', views.project, name="project"),
    path('task/<int:task_id>', views.task, name='task'),
    path('task/<int:task_id>/newcomment', views.newjournal, name='newjournal'),
    path('project/<int:proj_id>/newtask', views.newtask, name="newtask" ),
    path('task/<int:task_id>/edittask', views.edittask, name="edittask"),

]