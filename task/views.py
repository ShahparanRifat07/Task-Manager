from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from .models import Task,Image
from .forms import TaskForm
from .filters import TaskFilter


class TaskListView(LoginRequiredMixin,View):

    def get(self,request):
        task_filter = TaskFilter(request.GET, queryset=Task.objects.filter(user = request.user).order_by('created_at'))
        context ={
            "form" : task_filter.form,
            "tasks" : task_filter.qs,
        }
        return render(request, 'task/task_list.html',context)




class TaskCreateView(LoginRequiredMixin, View):

    def post(self,request):
        task_form = TaskForm(request.POST)
        images = request.FILES.getlist('images')
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.user = request.user
            task.save()
            for image in images:
                Image.objects.create(task = task, image = image)
            return redirect('task:task_list')
        else:
            messages.add_message(request, messages.INFO, "Form is not valid")
            return redirect('task:task_create')

    def get(self,request):
        task_form = TaskForm()
        context = {
            "form" : task_form,
        }
        return render(request, 'task/task_create.html',context)