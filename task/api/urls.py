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
)




urlpatterns = [
    path('tasks/',TaskListAPIView.as_view(),name='task_list'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
    path('tasks/create/', TaskCreateAPIView.as_view(), name='task_create'),
    path('tasks/<int:pk>/update/', TaskUpdateAPIView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteAPIView.as_view(), name='task_delete'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
