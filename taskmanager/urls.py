from django.urls import path
from . import views
urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<int:id>', views.project, name="project"),
    path('task/<int:id>', views.task, name='task'),
    path('newComment/<int:id>', views.newComment, name='newComment'),
]