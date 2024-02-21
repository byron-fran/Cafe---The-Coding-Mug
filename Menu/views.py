from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Menu
# Create your views here.
class MenuView(ListView):
    template_name = 'menu.html'
    model = Menu
    paginate_by = 12
    context_object_name = 'menu'
    def get_queryset(self):
        self.queryset = Menu.objects.all().order_by('-name')
        
    def get_context_data(self, **kwargs: Any):
        term = self.request.GET.get('search')
        if(term is not None):
            menu_filters = Menu.objects.filter(name__icontains=term)
            if(menu_filters):
                return {
                "menu": menu_filters
            }
            else:
                return {
                    "message": "No hay resultados"
                }    
        else:
            
            return {
                "menu" : self.queryset
            }
        
class MenuDetail(DetailView):
    model = Menu 
    template_name = 'menu_detail.html'
    context_object_name = 'dish'   
    

