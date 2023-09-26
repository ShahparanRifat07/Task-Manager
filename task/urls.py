from django.urls import path
from .views import (
   TaskCreateView,
   TaskListView
)

app_name ='task'

urlpatterns = [
    path('',TaskListView.as_view(),name='task_list'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
]