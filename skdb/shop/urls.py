from django import views
from django.urls import path
from . import views

urlpattern = [
    path('cstm/', views.customerinfo),
]