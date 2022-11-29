from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('learn_django/', views.learn_django, name='learn_django'),
    path('leran_python/', views.leran_python, name='leran_python'),
]
