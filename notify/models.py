from django.db import models

# Create your models here.
class Task(models.Model):

    task_type = models.IntegerField()
    task_desc = models.TextField()
    date = models.DateField(auto_now=True)


class TaskTracker(models.Model):

    DAILY = 'DAILY'
    WEEKLY = 'WEEKLY'
    MONTHLY = 'MONTHLY'
    STATUS = [
        (DAILY, ('DAILY')),
        (WEEKLY, ('WEEKLY')),
        (MONTHLY, ('MONTHLY')),
    ]

    task_type = models.IntegerField()
    update_type = models.CharField(
        max_length=10,
        choices=STATUS,
        default=DAILY,
    )
    email = models.EmailField(primary_key=True,max_length=254)    



    
