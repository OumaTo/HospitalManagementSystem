from django.urls import path
from HMS import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),

    path('login', views.login, name='login'),
    path('staff', views.staff, name='staff'),
    path('appointments', views.appointments, name='appointments'),


]