from django.shortcuts import render
from .forms import Inputform

# Create your views here.

def home(request):
    return render(request, "home.html")

# def  get_user(request): 
