from django.contrib import admin
from .views import Task,Image

# Register your models here.

admin.site.register(Image)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','user', 'due_date', 'priority', 'complete', 'created_at')
    list_filter = ('priority', 'complete', 'created_at', 'user')
    readonly_fields = ('title','user', 'description', 'due_date', 'priority', 'complete', 'created_at', 'updated_at') 
    ordering = ('priority',)