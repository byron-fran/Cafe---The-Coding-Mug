from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import User

from django.views.generic import FormView
from django.shortcuts import redirect, render  
from .forms import UserForm
from django.contrib.auth import login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


class Login(LoginView):
    template_name = 'registration/login.html'
    form_class = User
    redirect_authenticated_user = True
    



def signUp(request):
    if request.method == 'POST':
        form =   UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form =  UserForm()
    return render(request, 'registration/register.html', {'form' : form})    


def logout_view(request):
    logout(request)
    return redirect('login')