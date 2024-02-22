from django.urls import path
from Menu.models import Menu
from . import views

urlpatterns = [
    path('new_order/<str:id_menu>/', views.add_order, name="new_order"),
    path('list_orders/', views.OrdersView.as_view(), name='list_orders'),
    path('remove_order/<int:id_order>/', views.remove_order, name='remove_order'),
    path('create-checkout-session/', views.create_checkout_session, name='create-checkout-session'), # new
    path('success/', views.SuccessView.as_view(), name='success'), # new
    path('cancelled/', views.CancelledView.as_view())
]


