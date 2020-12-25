from django.urls import path, include
from notify import views

urlpatterns = [
    path('', views.login, name='login'),
]
