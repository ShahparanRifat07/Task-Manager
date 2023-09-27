from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import MultiPartParser, FormParser


from .serializers import TaskSerializer, ImageSerializer, ImageListSerializer
from task.models import Task,Image
from .permissions import TaskUserOrReadOnly


class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['due_date','priority','complete']
    search_fields = ['title',]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)
    

class TaskCreateAPIView(generics.CreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated,TaskUserOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskDetailAPIView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, TaskUserOrReadOnly]
    authentication_classes = [JWTAuthentication]


class TaskUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, TaskUserOrReadOnly]
    authentication_classes = [JWTAuthentication]


class TaskDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, TaskUserOrReadOnly]
    authentication_classes = [JWTAuthentication]



class ImageListAPIView(generics.ListAPIView):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated, TaskUserOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        task_pk = self.kwargs['pk']
        return Image.objects.filter(task_id=task_pk)



class ImageCreateAPIView(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageListSerializer
    permission_classes = [IsAuthenticated, TaskUserOrReadOnly]
    authentication_classes = [JWTAuthentication]
    parser_class = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save()


class ImageDeleteAPIView(generics.DestroyAPIView):
    queryset = Image.objects.all()
    permission_classes = [IsAuthenticated, TaskUserOrReadOnly]
    authentication_classes = [JWTAuthentication]
    lookup_url_kwarg = 'image_pk'
