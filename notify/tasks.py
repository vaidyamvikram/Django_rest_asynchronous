from __future__ import absolute_import, unicode_literals
from celery import shared_task,Celery,task
from .models import Task,TaskTracker
import time
from datetime import timedelta
import datetime
from django.core import serializers
from django.utils import timezone
    
def is_leap_year(year): 
    if (year % 4) == 0: 
        if (year % 100) == 0: 
            if (year % 400) == 0: 
                return True
            else: 
                return False
        else: 
             return True
    else: 
        return False

def get_lapse():
    last_month = timezone.now().date().month
    current_year = timezone.now().date().year

    #is last month a month with 30 days?
    if last_month in [9, 4, 6, 11]:
        lapse = 30

    #is last month a month with 31 days?
    elif last_month in [1, 3, 5, 7, 8, 10, 12]:
        lapse = 31

    #is last month February?
    else:
        if is_leap_year(current_year):
            lapse = 29
        else:
            lapse = 30

    return lapse


@shared_task
def send_daily_update():
    today=datetime.datetime.now()
    tasktracker_all = serializers.serialize("json",TaskTracker.objects.filter(update_type='DAILY'))
    tasktracker_all = serializers.deserialize("json",tasktracker_all)
    for i in tasktracker_all:
        data=serializers.serialize("json",Task.objects.filter(date=today,task_type=i.object.task_type))
        a=serializers.deserialize("json",data)
        for z in a:
            print(z.object.task_desc)
    


@shared_task
def send_weekly_update():
    today=datetime.datetime.now()
    tasktracker_all = serializers.serialize("json",TaskTracker.objects.filter(update_type='WEEKLY'))
    tasktracker_all = serializers.deserialize("json",tasktracker_all)
    for i in tasktracker_all:
        data=serializers.serialize("json",Task.objects.filter(date=today,task_type=i.object.task_type))
        a=serializers.deserialize("json",data)
        for z in a:
            print(z.object.task_desc)

@shared_task
def send_monthly_update():
    today=datetime.datetime.now()
    tasktracker_all = serializers.serialize("json",TaskTracker.objects.filter(update_type='MONTHLY'))
    tasktracker_all = serializers.deserialize("json",tasktracker_all)
    for i in tasktracker_all:
        data=serializers.serialize("json",Task.objects.filter(date=today,task_type=i.object.task_type))
        a=serializers.deserialize("json",data)
        for z in a:
            print(z.object.task_desc)
