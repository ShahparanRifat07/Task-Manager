from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    TaskListAPIView,
    TaskCreateAPIView,
    TaskUpdateAPIView,
)




urlpatterns = [
    path('tasks/',TaskListAPIView.as_view(),name='task_list'),
    path('tasks/create/', TaskCreateAPIView.as_view(), name='task_create'),
    path('task/<int:pk>/update/', TaskUpdateAPIView.as_view(), name='task_update'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
