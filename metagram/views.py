from django.shortcuts import render
from .forms import User, authenticate,login

# Create your views here.


def home(request):
    return render(request, "home.html")


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    username = authenticate(username=username, password=password)
    if User is not None:
        login(request, User)
        # redirect to home page when user is logged in
        return render(request, "home.html")
    else:
    # redirect to login page when user is not logged in
        return render(request, "login.html", {'form': User()})


def signup(request):
    return render(request, "signup.html")


def display(request):
    return render(request, "display.html")


def bio(request):
    return render(request, "bio.html")


def get_user(request):
    if request.method == "POST":
        form = Inputform(request.POST)
        if form.is_valid():
            return render(request, "login.html", {'form': form})
    else:
        return render(request, "login.html", {'form': Inputform()})
