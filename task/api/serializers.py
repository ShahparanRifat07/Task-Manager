from rest_framework import serializers
from user.models import User
from task.models import Task, Image

class ImageListSerializer(serializers.Serializer):
    images = serializers.ListField(child=serializers.ImageField(allow_empty_file=False),write_only=True)

    def create(self, validated_data):
        task_pk = self.context['view'].kwargs.get('pk')
        task = Task.objects.get(pk = task_pk)
        images_data = validated_data.pop('images')
        images = []
        
        for image in images_data:
            image = Image.objects.create(task=task, image=image)
            images.append(image)
        
        return images


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