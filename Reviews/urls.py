from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.FormReview.as_view(), name='add_comment')    
]
