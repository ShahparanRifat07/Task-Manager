from django.urls import path
from .views import (
    task_list,TaskCreateView
)

app_name ='task'

urlpatterns = [
    path('',task_list,name='task_list'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
]