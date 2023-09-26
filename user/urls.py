from django.urls import path,reverse_lazy
from django.contrib.auth import views as auth_views
from .views import (
    LoginView,
    RegisterView,
    UserLogoutView
)

app_name ='user'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="auth/password_reset.html",
            success_url=reverse_lazy('user:password_reset_done'),
            email_template_name = "auth/password_reset_email.html"
            ),
        name='password_reset'
    ),

    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(template_name="auth/password_reset_sent.html"),
        name='password_reset_done'
    ),

    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="auth/password_reset_form.html",
            success_url=reverse_lazy('user:password_reset_complete'),
        ),
        name='password_reset_confirm'
    ),

    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="auth/password_reset_done.html",
        ),
        name='password_reset_complete'
    ),


]