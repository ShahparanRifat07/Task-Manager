from rest_framework import serializers
from user.models import User
from task.models import Task, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = ['task']

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    images = ImageSerializer(many=True,read_only=True)
    class Meta:
        model = Task
        fields = "__all__"