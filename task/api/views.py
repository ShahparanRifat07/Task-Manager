from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework_simplejwt.authentication import JWTAuthentication


from .serializers import TaskSerializer
from task.models import Task
from .permissions import TaskUserOrReadOnly


class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated,TaskUserOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)


