from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import  Loginform,RegisterForm
# Create your views here.


def home(request):
    return render(request, "home.html")


def login(request):
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                return redirect(request, "display.html", {'form': form})
    else:
        form = Loginform()
    return render(request, "login.html", {'form': form})




def display(request):
    return render(request, "display.html")


def bio(request):
    return render(request, "bio.html")


def logout(request):
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, "registration/signup.html", {'form': form})
