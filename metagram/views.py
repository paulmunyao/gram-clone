from django.shortcuts import render
from .forms import User, authenticate,login

# Create your views here.


def home(request):
    return render(request, "home.html")


def login(request):
    if request.method == 'POST':
        form = User(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "login.html")
    else:
        form = User()   
    return render(request, "login.html", {'form': form})

def signup(request):
    if request.method =="POST":
        form = User(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"signup.html")
    else:
        form = User()
        
    


def display(request):
    return render(request, "display.html")


def bio(request):
    return render(request, "bio.html")

