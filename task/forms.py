from django import forms
from .models import Task
from django.forms.widgets import NumberInput

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'complete']
