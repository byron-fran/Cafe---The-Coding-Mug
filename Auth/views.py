from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import User

from django.views.generic import FormView
from django.shortcuts import redirect  
from .forms import UserForm
from django.contrib.auth import login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


class Login(LoginView):
    template_name = 'registration/login.html'
    form_class = User
    redirect_authenticated_user = True
    
class Register(FormView):
    template_name = 'registration/register.html'
    form_class = UserForm
    redirect_authenticated_user = True
    login_url = reverse_lazy('')  
    def test_func(self):
  
        return not self.request.user.is_authenticated

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('')
    


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')