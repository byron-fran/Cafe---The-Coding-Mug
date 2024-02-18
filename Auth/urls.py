from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('signup/', views.Register.as_view(), name='signup'),    
    
]
