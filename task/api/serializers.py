from rest_framework import serializers
from user.models import User
from task.models import Task, Image


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Task
        fields = "__all__"