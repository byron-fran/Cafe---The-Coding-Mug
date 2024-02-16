from django.shortcuts import render

# Create your views here.
from django.http import request
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')