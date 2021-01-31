from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.core.exceptions import ObjectDoesNotExist
from .forms import LoginForm
from .models import Notification
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
            try:
                incoming_notifications = Notification\
                    .get_incoming_notifications(user)
                outgoing_notifications = Notification\
                    .get_outgoing_notifications(user)
                context = {
                    "incoming": incoming_notifications,
                    "outgoing": outgoing_notifications
                }
            except ObjectDoesNotExist:
                context = {
                    "incoming": [],
                    "outgoing": []
                }
            return render(request, 'dashboard.html', context)
        else:
            return render(request, 'login.html', context)

    return render(request, 'login.html', context)


def logout(request):
    auth_logout(request)
    return render(request, 'home.html')


def dashboard(request):
    # Update: List of notifications
    # Update: List of

    if request.user:
        outgoing_notifications = Notification.get_outgoing_notifications(
            request.user)
        incoming_notifications = Notification.get_incoming_notifications(
            request.user)
        context = {
            "incoming": incoming_notifications,
            "outgoing": outgoing_notifications
        }
        return render(request, 'dashboard.html', context)
    else:
        return render(request, 'login.html', context)
