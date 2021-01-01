from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.


def home(request):
    if request.method == "GET":
        return render(request, 'home.html')


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            context = {
                "user": user
            }
            return render(request, 'dashboard.html', context)
        else:
            print("Error")
            # UPDATE: notification for error -wrong username or password

    return render(request, 'login.html', context)
