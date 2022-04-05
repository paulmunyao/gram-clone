from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .models import images
# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, "registration/signup.html", {'form': form})

def display(request):
    return render(request, "display.html")

@login_required(login_url='login/')
def home(request):
    posts = images.objects.all()
    return render(request, "home.html", {'images': posts})

