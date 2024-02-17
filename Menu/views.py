from django.shortcuts import render
from django.views.generic import ListView
from .models import Menu
# Create your views here.
class Menu(ListView):
    template_name = 'menu.html'
    model = Menu
    paginate_by = 12
    context_object_name = 'menu'
    