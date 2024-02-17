from django.urls import path
from . import views
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('home/', home, name='home'),
    path('signup/', views.Register.as_view(), name='signup'),
    
    
]
