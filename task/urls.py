from django.urls import path
from .views import (
    task_list
)

app_name ='task'

urlpatterns = [
    path('',task_list,name='task_list'),
]