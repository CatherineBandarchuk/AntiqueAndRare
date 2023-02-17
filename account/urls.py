from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'account'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(template_name='account/signup.html'), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', views.logOut, name='logout'),    
]