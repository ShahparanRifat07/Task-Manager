from django.shortcuts import render,redirect,get_object_or_404
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


class TaskDetailView(LoginRequiredMixin,View):

    def get(self,request,pk):
        task = get_object_or_404(Task, pk=pk)
        images = Image.objects.filter(task = task)
        context ={
            "task" : task,
            "images" : images,
        }
        return render(request, 'task/task_detail.html',context)



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



class TaskUpdateView(LoginRequiredMixin, View):

    def post(self,request,pk):
        task = get_object_or_404(Task, pk=pk)
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('task:task_detail', pk=task.pk)
        else:
            messages.add_message(request, messages.INFO, "Form is not valid")
            return redirect('task:task_update', pk=task.pk)

    def get(self,request,pk):
        task = get_object_or_404(Task, pk=pk)
        task_form = TaskForm(instance=task)
        images = Image.objects.filter(task=task)
        context = {
            "form" : task_form,
            "task" : task,
            "images" : images,
        }
        return render(request, 'task/task_update.html',context)



class TaskDeleteView(LoginRequiredMixin, View):
    def post(self,request,pk):
        task = get_object_or_404(Task, pk=pk)
        images = Image.objects.filter(task=task)
        if images:
            for image in images:
                image.image.delete()
                image.delete()
        task.delete()
        return redirect('task:task_list')

    def get(self,request,pk):
        task = get_object_or_404(Task, pk=pk)
        context = {
            "task" : task,
        }
        return render(request, 'task/task_delete.html',context)


class TaskImageCreateView(LoginRequiredMixin, View):
    def post(self,request,pk):
        task = get_object_or_404(Task, pk=pk)
        images = request.FILES.getlist('images')
        for image in images:
            Image.objects.create(task = task, image = image)
        return redirect('task:task_update', pk=task.pk)


class TaskImageDeleteView(LoginRequiredMixin, View):
    def post(self,request,pk,image_pk):
        task = get_object_or_404(Task, pk=pk)
        image = get_object_or_404(Image, pk=image_pk)

        if image.task == task:
            image.image.delete()
            image.delete()
        return redirect('task:task_update', pk=task.pk)
