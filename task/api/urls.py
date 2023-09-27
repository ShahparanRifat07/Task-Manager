from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    TaskListAPIView,
    TaskDetailAPIView,
    TaskCreateAPIView,
    TaskUpdateAPIView,
    TaskDeleteAPIView,

    ImageListAPIView,
    ImageCreateAPIView,
    ImageDeleteAPIView,
)




urlpatterns = [
    path('tasks/',TaskListAPIView.as_view(),name='task_list'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
    path('tasks/create/', TaskCreateAPIView.as_view(), name='task_create'),
    path('tasks/<int:pk>/update/', TaskUpdateAPIView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteAPIView.as_view(), name='task_delete'),

    path('tasks/<int:pk>/images/', ImageListAPIView.as_view(), name='task_image_list'),
    path('tasks/<int:pk>/images/create/', ImageCreateAPIView.as_view(), name='task_image_create'),
    path('tasks/<int:pk>/images/<int:image_pk>/delete/', ImageDeleteAPIView.as_view(), name='task_image_delete'),


    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
