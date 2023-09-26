from django.db import models
from django.utils import timezone


from user.models import User
from .helpers import generate_unique_filename
# Create your models here.

class Task(models.Model):
    class PriorityChoices(models.TextChoices):
        LOW = 'L'
        MEDIUM = 'M'
        HIGH = 'H'
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    priority = models.CharField(max_length=1,choices=PriorityChoices.choices)
    complete = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Image(models.Model):
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True,upload_to=generate_unique_filename)

    def __str__(self):
        return self.task.title


