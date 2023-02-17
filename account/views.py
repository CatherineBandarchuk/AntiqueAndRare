from django.shortcuts import redirect 
from .forms import CustomUserCreationForm
from django.contrib.auth import logout

from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("account:login")
    template_name = "/signup.html"


def logOut(request):
    logout(request)
    return redirect('main:index')