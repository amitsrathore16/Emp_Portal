from django.urls import path
from django.contrib.auth import views as v
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('view/', views.view, name='view'),
]
