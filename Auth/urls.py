from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from App import settings


urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('signup/', views.signUp, name='signup'),   
    path('logout', views.logout_view, name='account_logout') 
    
]
