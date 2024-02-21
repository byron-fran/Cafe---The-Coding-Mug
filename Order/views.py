from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from .models import Order
from django.http import HttpResponse
from Menu.models import Menu
from django.views.generic import ListView

# Create your views here.
def add_order(request, id_menu):
    
    menu_found = Menu.objects.get(id=id_menu)
  
    order, created = Order.objects.get_or_create(
        user=request.user,
        name = menu_found.name,
        price = menu_found.price,
        image = menu_found.image,
        description = menu_found.description,
        quantity = 1
        
        
    )
    # Agregar el producto a la relación ManyToManyField
    order.menu.add(menu_found)    
    return redirect('list_orders')

def remove_order(request, id_order):
    order_found = Order.objects.get(id=id_order)
    order_found.delete()
    return redirect('list_orders')

class Orders(LoginRequiredMixin, ListView):
    login_url = '/accounts/login'
    template_name = 'orders.html'
    context_object_name = 'orders'
    model = Order
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = context['orders'].filter(user=self.request.user)
        return context
    