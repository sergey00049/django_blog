from django.urls import path
from . import views as userViews
from django.contrib.auth import views as authViews

urlpatterns = [
    path('reg/', userViews.register, name = 'reg'),
    path('auth/', authViews.LoginView.as_view(template_name = 'user/login.html'), name = 'login'),
    path('exit/', authViews.LogoutView.as_view(template_name = 'user/exit.html'), name = 'exit'),
    path('profile/', userViews.profile, name = 'profile'),
]