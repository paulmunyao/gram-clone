from django.shortcuts import render
from .forms import Inputform

# Create your views here.

def home(request):
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")   

def signup(request):
    return render(request, "signup.html")     

def  get_user(request):
    if request.method == "POST":
        form = Inputform(request.POST)
        if form.is_valid():
            return render (request,"login.html",{'form':form})
    else:
        return render(request, "login.html", {'form':Inputform()})

