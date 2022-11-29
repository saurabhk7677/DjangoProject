from django.urls import path
from course import views

urlpatterns = [
    path('learnd/', views.learn_django_dj),
    path('learnp/', views.learn_python_dj),
    path('learndj/', views.learn_django),
    path('learnpy/', views.learn_python),
]