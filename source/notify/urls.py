from django.urls import path
from notify import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]
