from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskTrackerSerializer,TaskSerializer
from .models import TaskTracker,Task
import datetime
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def url_details(request):
    url_list = {
        'To check tasklist':'/tasklist/',
        'To check tasktrackerlist':'/tasktrackerlist/',
        'To create a task':'/taskcreate/',
        'To create a tasktracker':'/tasktrackercreate/',
        'To update a task':'/taskupdate/<int:task_typr>/<str:task_desc>',
    }
    return Response(url_list)

@api_view(['GET'])
def tasklist(request):
    task_list = Task.objects.all()
    serializer = TaskSerializer(task_list,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def taskcreate(request):
    serializer = TaskSerializer(data=request.data)
    task_list = Task.objects.all()
    count=0
    for i in task_list:
        if request.data['task_type'] == i.task_type and request.data['task_desc'] == i.task_desc:
            count+=1
    if count==0:
        if serializer.is_valid():
            serializer.save()
    else:
        return Response("This task is already exists")
    return Response(serializer.data)

@api_view(['GET','POST'])
def taskupdate(request,task_type,task_desc):
    task = Task.objects.get(task_type=task_type,task_desc=task_desc)
    serializer = TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def taskupdatenull(request):
    return Response("Enter the description to be updated in the url")

@api_view(['POST'])
def tasktrackercreate(request):
    serializer = TaskTrackerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response("Email is already exists")
    return Response(serializer.data)

@api_view(['GET'])
def tasktrackerlist(request):
    task_list = TaskTracker.objects.all()
    serializer = TaskTrackerSerializer(task_list,many=True)
    return Response(serializer.data)