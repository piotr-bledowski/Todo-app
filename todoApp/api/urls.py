from django.urls import path

from . import views

urlpatterns = [
    path('todo-api/', views.todoApi, name='todo-api'),
    path('task-all/', views.taskAll, name='task-all'),
    path('task-todo/', views.taskTodo, name='task-todo'),
    path('task-completed/', views.taskCompleted, name='task-completed'),
    path('task-detail/<str:pk>/', views.taskDetail, name='task-detail'),
    path('task-add/', views.taskAdd, name='task-add'),
    path('task-update/<str:pk>/', views.taskUpdate, name='task-update'),
    path('task-delete/<str:pk>/', views.taskDelete, name='task-delete'),
    path('task-complete/<str:pk>/', views.taskComplete, name='task-complete'),
]
