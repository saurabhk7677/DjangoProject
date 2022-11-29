from django.shortcuts import HttpResponse, render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Home Page')
    
def learn_django(request):
    return HttpResponse('Hello Django')

def leran_python(request):
    return HttpResponse('<h1>Hello Python</h1>')