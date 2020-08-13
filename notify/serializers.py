# serializers.py
from rest_framework import serializers

from .models import TaskTracker,Task

class TaskTrackerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TaskTracker
        fields = ('task_type','update_type','email')

class TaskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Task
        fields = ('task_type','task_desc')