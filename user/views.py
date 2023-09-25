from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate



#custom imports
from .helpers import isEmpty,checkUserExists
from .models import User


# Create your views here.


class LoginView(View):

    def post(self, request):
        if not request.user.is_authenticated:
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(email= email,password = password)

            if user is not None:  
                login(request,user)
                return redirect("task:task_list")
            else:
                messages.add_message(request, messages.INFO, "User Not Found")
                return redirect("user:login")
        else:
            return redirect("task:task_list")

    def get(self, request):
        return render(request, 'auth/login.html')
    





class RegisterView(View):

    def post(self, request):
        if not request.user.is_authenticated:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')

            if isEmpty(first_name,last_name,email,password):
                messages.add_message(request, messages.INFO, "Fields can't be empty")
                return redirect('user:register')
            
            else:
                if checkUserExists(email) is True:
                    messages.add_message(request, messages.INFO, "This email is already in use.")
                    return redirect('user:register')
                else:
                    user = User(first_name = first_name,last_name = last_name,username = email, email =email)
                    user.set_password(password)
                    user.save()
                    return redirect('user:login')
        else:
            return redirect('task:task_list')

    def get(self, request):
        return render(request, 'auth/register.html')