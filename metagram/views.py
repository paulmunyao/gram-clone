from django.shortcuts import render
from .forms import LoginForm, Signupform

# Create your views here.


def home(request):
    return render(request, "home.html")


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "display.html", {'form': form})
    else:
        form = LoginForm()
    return render(request, "login.html", {'form': form})


def signup(request):
    if request.method == "POST":
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "login.html", {'form': form})
    else:
        form = Signupform()
    return render(request, "signup.html", {'form': form})


def display(request):
    return render(request, "display.html")


def bio(request):
    return render(request, "bio.html")
