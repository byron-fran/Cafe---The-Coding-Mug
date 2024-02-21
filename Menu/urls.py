from django.urls import path
from . import views
from .models import Menu

urlpatterns = [
    path('menu/', views.Menu.as_view(), name='menu'),
    path('menu/<slug:slug>/', views.MenuDetail.as_view(model=Menu), name='menu_detail')
]
