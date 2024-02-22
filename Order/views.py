from typing import Any
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from .models import Order
from django.http import HttpResponse
from Menu.models import Menu
from django.views.generic import ListView, TemplateView
from django.conf import settings
import stripe

# Create new order.
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

    order.menu.add(menu_found)    
    return redirect('list_orders')


#remove order by id
def remove_order(request, id_order):
    order_found = Order.objects.get(id=id_order)
    order_found.delete()
    return redirect('list_orders')

class OrdersView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login'
    template_name = 'orders.html'
    context_object_name = 'orders'
    model = Order
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = context['orders'].filter(user=self.request.user)
        return context


#Payments
def create_checkout_session(request):
    orders_by_user = Order.objects.filter(user=request.user)    
    line_items = []
            
    for order in orders_by_user:
        line_item = {
            'price_data': {
             'currency': 'usd',
             'unit_amount': order.price * 100,
                'product_data': {
                    'name': f'Order #{order.name}',
                    'description': f'Order #{order.name}',
                    'images' : [order.image.url]
                },
            },
            'quantity': 1,
        }
        
        line_items.append(line_item)
        
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/' 
        #Todo: cambiar por las variables de entorno   
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'orders/success/?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'orders/cancelled/',
                payment_method_types=['card'], 
                mode='payment',

                line_items = line_items
            )
           
            return redirect(checkout_session.url)
        except Exception as e:
           return JsonResponse({'error': str(e)})
       
class SuccessView(TemplateView):
    template_name = 'success.html'    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        if self.request.method == 'GET':
            session_id = self.request.GET.get('session_id')
            print(session_id)
            return {
                "token" : session_id
            }


class CancelledView(TemplateView):
    template_name = 'cancelled.html'       