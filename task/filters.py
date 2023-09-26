import django_filters
from django import forms
from django.forms.widgets import NumberInput
from .models import Task

class TaskFilter(django_filters.FilterSet):
    due_date = django_filters.DateFilter(widget=NumberInput(attrs={'type': 'date'}))
    created_at = django_filters.DateFilter(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = Task
        fields = {
            'title': ['icontains'],
            'due_date': ['exact'],
            'priority': ['exact'],
            'complete': ['exact'],
            'created_at' : ['exact'],
            }