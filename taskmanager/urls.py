from django.urls import path
from . import views
urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<int:id>', views.project, name="project"),
    path('task/<int:id>', views.task, name='task'),
    path('task/<int:id>/newcomment', views.newComment, name='newComment'),
    path('project/<int:id>/newtask', views.newtask, name="newtask" )
]