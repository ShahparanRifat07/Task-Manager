from functools import wraps
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from .models import Task

def user_is_task_owner(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        if task.user == request.user:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You don't have permission to access this task.")
    return _wrapped_view