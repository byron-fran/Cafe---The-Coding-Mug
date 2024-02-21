from .models import Order

def total_quantity(request):
    total = 0
    user = request.user
    if user.is_authenticated:
        user_orders = Order.objects.filter(user=user)
        for order in user_orders:
            total += order.price
    
        return {
            "total" : total
       
        }
    else:    
        return {
         
        }   