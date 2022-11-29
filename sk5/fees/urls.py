from django.urls import path
from . import views

urlpatterns = [
    path('feedj/', views.fees_django),
]