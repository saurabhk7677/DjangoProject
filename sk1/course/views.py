from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_django_dj(request):
    return HttpResponse('Hello Django')

def learn_python_dj(request):
    return HttpResponse('Hello python') 


def learn_django(request):
    return render(request, 'courseone.html')

def learn_python(request):
    return render(request, 'coursetwo.html') 
