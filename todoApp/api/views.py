from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer
import json

# Create your views here.


@api_view(['GET'])
def todoApi(request):
    api_urls = {
        'All tasks': '/task-all/',
        'Tasks to do': '/task-todo/',
        'Completed tasks': '/task-completed',
        'Particular task': '/task-detail/<str:pk>/',
        'Add task': '/task-add/',
        'Update task': '/task-update/<str:pk>/',
        'Delete task': '/task-delete/<str:pk>/',
        'Complete task': '/task-complete/<str:pk>/'
    }
    return Response(api_urls)


@api_view(['GET'])
def taskAll(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskTodo(request):
    tasks = Task.objects.filter(completed=False)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskCompleted(request):
    tasks = Task.objects.filter(completed=True)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskAdd(request):
    # here be dragons
    print(request.body.decode('utf-8'))
    serializer = TaskSerializer(data=json.loads(request.body.decode('utf-8')))
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response('INVALID DATA')


@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response('INVALID DATA')


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Task deleted successfully')


@api_view(['POST'])
def taskComplete(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(
        instance=task, data=json.loads(request.body.decode('utf-8')))
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response('INVALID DATA')
