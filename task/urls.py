from django.urls import path
from .views import (
   TaskCreateView,
   TaskListView,
   TaskDetailView,
   TaskUpdateView,
   TaskImageCreateView,
   TaskImageDeleteView,
   TaskDeleteView,
)

app_name ='task'

urlpatterns = [
    path('',TaskListView.as_view(),name='task_list'),
    path('task/<int:pk>',TaskDetailView.as_view(),name='task_detail'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/update/<int:pk>', TaskUpdateView.as_view(), name='task_update'),
    path('task/delete/<int:pk>', TaskDeleteView.as_view(), name='task_delete'),
    path('task/update/<int:pk>/image/add/', TaskImageCreateView.as_view(), name='task_image_add'),
    path('task/update/<int:pk>/image/delete/<int:image_pk>', TaskImageDeleteView.as_view(), name='task_image_delete'),
]