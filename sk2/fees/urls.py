from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feedj/', views.fees_django),
    path('feepy/', views.fees_python),
    path('feedh/', views.f_django),
    path('feeph/', views.f_python),
]
