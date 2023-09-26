from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

# admin.site.register(User, UserAdmin)

@admin.register(User)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name', 'email', 'is_staff')
    list_filter = ('email', 'first_name','last_name')
    readonly_fields = ('first_name','last_name', 'username', 'email','last_login', 'date_joined','password') 
