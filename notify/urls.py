
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('',views.url_details,name="url_details"),
    path('tasklist/', views.tasklist,name="tasklist"),
    path('tasktrackerlist/', views.tasktrackerlist,name="tasktrackerlist"),
    path('taskcreate/', views.taskcreate,name="taskcreate"),
    path('taskupdate/', views.taskupdatenull,name="taskupdatenull"),
    path('taskupdate/<int:task_type>/<str:task_desc>/', views.taskupdate,name="taskupdate"),
    path('tasktrackercreate/', views.tasktrackercreate,name="tasktrackercreate"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
